from typing import List, Dict, Optional, Type
from Terminal import Builder, Utils, Terminal
import sys

class Page:
    game: "Game"
    def __init__(self) -> None:
        self.builder = Builder()
    @property
    def manager(self) -> "Manager":
        return self.game.manager
    def init(self, game: "Game") -> None:
        self.game = game
    def render(self) -> None:
        ...

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
    pages: Dict[str, Page]

    @classmethod
    def build(cls, pages: Dict[str, Type[Page]]) -> None:
        cls.pages = {k: v() for k, v in pages.items()}

    @classmethod
    def load(cls, game: "Game") -> None:
        game.manager.pages = cls.pages.copy()

class Manager:
    pages: Dict[str, Page]
    game: "Game"

    def __init__(self, game: "Game") -> None:
        self.game = game

    def init(self, name: str):
        if not self.game or not self.pages: return
        page = self.pages.get(name)
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