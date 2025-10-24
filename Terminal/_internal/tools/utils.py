from typing import List, Optional
from ..core import Terminal
from ..builder import Builder

__all__ = ("Utils",)

class Utils:
    builder = Builder() # All utils that prints more than a few times, will use this builder

    @classmethod
    def select_menu(cls, options: List[str], title: str = "Menu", prompt: str = "Select: ", *, color: bool = False) -> str:
        cls.builder.print(title)
        cls.builder.value += "\n".join(options)
        cls.builder.render(color=color)
        cls.builder.clear()
        return Terminal.input(prompt, color=color)
    
    @classmethod
    def confirm(cls, prompt: str, yes: List[str] = ["y", "yes"], no: List[str] = ["n", "no"], *, color: bool = False) -> Optional[bool]:
        user_input = Terminal.input(prompt, color=color).lower()
        return True if user_input in yes else False if user_input in no else None