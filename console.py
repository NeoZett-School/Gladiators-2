from typing import List, Dict, Optional, Type
from Terminal import Builder, Utils, Terminal
import sys

class Page:
    game: "Game"
    tag: str = "UnTagged"
    children_loaded: bool = False
    children_classes: List[Type["SubPage"]] = []
    children_instances: List["SubPage"]
    def __init__(self, tag: Optional[str] = None) -> None:
        self.tag = tag or self.__class__.tag
        self.children_instances = []
        self.builder = Builder()
    @property
    def manager(self) -> "Manager":
        return self.game.manager
    def init(self, game: "Game") -> None:
        if not self.children_loaded:
            self._load_children()
        self.game = game
    def _load_children(self) -> None:
        if self.children_loaded: return
        self.children_instances = list(child(self) for child in self.__class__.children_classes)
        self.children_loaded = True
    def render(self) -> None:
        ...
    @classmethod
    def set_children(cls, children: List[Type["SubPage"]]) -> None:
        cls.children_classes.extend(children)

class SubPage(Page):
    parent: Page
    def __init__(self, parent: Page, tag: Optional[str] = None) -> None:
        super().__init__(self.full_tag(parent, tag))
        self.parent = parent
    @classmethod
    def full_tag(cls, parent: Page, tag: Optional[str] = None) -> str:
        return parent.tag + "." + tag or cls.tag

class MenuPage(Page):
    title: str
    subtitle: str
    prompt: str
    options: List[str]
    def init(self, game: "Game") -> None:
        super().init(game)
        self.build_ui()
    def build_ui(self) -> None:
        self.builder.clear()
        self.builder.print(self.title, color=True)
        self.builder.space()
    def generate_options(self, additional_text: Optional[List[str]] = None) -> str:
        return Utils.select_menu([
            f"$blu{i+1}$res: {v}{additional_text[i] if additional_text and len(additional_text) > i else ""}" for i, v in enumerate(self.options)
        ], title=self.subtitle, prompt=self.prompt, color=True)

class PageRegistry:
    pages: List[Type[Page]] = []

    @classmethod
    def build(cls, *args: Type[Page], pages: Optional[List[Type[Page]]] = None) -> None:
        cls.pages = list(args) + list(pages or [])

    @classmethod
    def load(cls, game: "Game") -> None:
        game.manager.manifest(cls.pages)

class Manager:
    page_classes: Dict[str, Type[Page]]
    page_instances: Dict[str, Page] = {}
    game: "Game"

    manifested: bool = False

    def __init__(self, game: "Game") -> None:
        self.game = game
    
    def manifest(self, pages: List[Type[Page]]) -> None:
        self.page_classes = {page.tag: page  for page in pages}
        self.manifested = True
    
    def _register_page(self, page: Page) -> None:
        if not page.tag in self.page_instances:
            self.page_instances[page.tag] = page
        for child in page.children_instances:
            self._register_page(child)
    
    def _load_page(self, name: str) -> Optional[Page]:
        if name in self.page_instances:
            return self.page_instances[name]
        if name in self.page_classes:
            page = self.page_classes[name]()
            self._register_page(page)
            return page
        return None

    def init(self, name: str) -> None:
        if not self.manifested: return
        page = self._load_page(name)
        if not page: return
        self.game.init_page(page)

class Game:
    def __init__(self) -> None:
        self.active: bool = False
        self.manager: Manager = Manager(self)
        self.page: Optional[Page] = None
        self.clear: bool = True
    
    def init_page(self, page: Page) -> None:
        self.page = page
        page.init(self)
    
    def init(self, name: str) -> None:
        self.manager.init(name)
    
    def render(self) -> None:
        if self.clear:
            Terminal.clear()
        if self.page: 
            self.page.render()
    
    def start(self) -> None:
        self.active = True
        while self.active:
            self.render()
        sys.exit(0) # Automatically deinitializes the Terminal
    
    def quit(self) -> None:
        self.active = False