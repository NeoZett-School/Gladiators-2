"""
The pages will allow you to make the application adaptive, modular, and dynamic.
"""

from typing import List, Dict, Optional, Type, Protocol 
from .builder import Builder

class Page(Protocol):
    """A page lets you create modular sections of your application."""
    app: "Application"
    tag: str
    children_loaded: bool
    children_classes: List[Type["SubPage"]]
    children_instances: List["SubPage"]
    builder: Builder

    def __init__(self, tag: Optional[str] = None) -> None: 
        ...

    @property
    def manager(self) -> "Manager": 
        """The manager of this application."""
        ...

    def init(self, app: "Application") -> None: 
        """Once the applciation initializes this page, it will call this method."""
        ...

    def _load_children(self) -> None: 
        ...

    def render(self) -> None: 
        """Render the page content."""
        ...

    @classmethod
    def set_children(cls, children: List[Type["SubPage"]]) -> None: 
        """Set the children of this page."""
        ...

class SubPage(Page):
    """A subpage is a page that is a child of another page."""
    parent: Page

    def __init__(self, parent: Page, tag: Optional[str] = None) -> None: 
        ...

    @classmethod
    def full_tag(cls, parent: Page, tag: Optional[str] = None) -> str: 
        ...

class MenuPage(Page):
    """A menu page is a page that displays a menu to the user."""
    title: str
    subtitle: str
    prompt: str
    options: List[str]

    def init(self, app: "Application") -> None: 
        ...

    def build_ui(self) -> None: 
        ...

    def generate_options(self, additional_text: Optional[List[str]] = None) -> str: 
        ...

class PageRegistry:
    """A registry to hold all pages for the application."""
    pages: List[Type[Page]]

    @classmethod
    def build(cls, *args: Type[Page], pages: Optional[List[Type[Page]]] = None) -> None: 
        """Build the page registry with the given pages."""
        ...

    @classmethod
    def load(cls, app: "Application") -> None: 
        """Load the pages into the application's manager."""
        ...

class Manager:
    """Manages the pages of the application."""
    page_classes: Dict[str, Type[Page]]
    page_instances: Dict[str, Page]
    app: "Application"
    manifested: bool

    def __init__(self, app: "Application") -> None:
        ...

    def manifest(self, pages: List[Type[Page]]) -> None:
        """Manifest the given pages into the manager."""
        ...

    def _register_page(self, page: Page) -> None:
        ...

    def _load_page(self, name: str) -> Optional[Page]:
        ...

    def init(self, name: str) -> None:
        """Initialize the page with the given name."""
        ...

class Application:
    """The main application class that uses pages to structure its content."""
    active: bool
    manager: Manager
    page: Optional[Page]
    clear: bool

    def __init__(self) -> None:
        ...

    def init_page(self, page: Page) -> None:
        """Initialize the given page as the current page."""
        ...

    def init(self, name: str) -> None:
        """Initialize the application with the page of the given name."""
        ...

    def render(self) -> None:
        """Render the current page."""
        ...

    def start(self) -> None:
        """Start the application loop."""
        ...

    def quit(self) -> None:
        """Quit the application."""
        ...

class Public:
    """
    The pages will allow you to make the application adaptive, modular, and dynamic.
    """
    Page: Type["Page"]
    SubPage: Type["SubPage"]
    MenuPage: Type["MenuPage"]
    PageRegistry: Type["PageRegistry"]
    Manager: Type["Manager"]
    Application: Type["Application"]