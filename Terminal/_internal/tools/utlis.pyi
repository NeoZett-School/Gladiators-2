from typing import List, Optional
from ..builder import Builder

class Utils:
    builder: Builder

    @classmethod
    def select_menu(cls, options: List[str], title: str = "Menu", prompt: str = "Select: ", *, color: bool = False) -> str:
        """Generate a menu for selecting one of the options."""
        ...
    
    @classmethod
    def confirm(cls, prompt: str, yes: List[str] = ["y", "yes"], no: List[str] = ["n", "no"], *, color: bool = False) -> Optional[bool]:
        """Get a confirmation from the user."""
        ...