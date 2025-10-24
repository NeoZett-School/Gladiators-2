from typing import List, Optional
from .core import ClearScreenArg

class BuilderString:
    content: List[str]
    index: int

    def __init__(self, *args: str) -> None:
        ...

    @property
    def value(self) -> str:
        """The current value."""
    
    @value.setter
    def value(self, new: str) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __getitem__(self, index: int) -> str:
        ...
    
    def __setitem__(self, index: int, value: str) -> None:
        ...
    
    def get(self, index: int) -> str:
        """Get this index of content."""
        ...

class Builder:
    """Use the builder to build your page before you print it."""

    def __init__(self, value: str = "") -> None:
        ...
    
    def next(self) -> None:
        """Move to the next page."""
        ...
    
    def prev(self) -> None:
        """Move to the previous page."""
        ...
    
    def clear_all(self) -> None:
        """Clear all pages."""
        ...

    @property
    def value(self) -> str:
        """The currently displayed value."""
        ...
    
    @value.setter
    def value(self, text: str) -> None:
        ...
    
    @property
    def index(self) -> int:
        """The index of the content displayed."""
        ...
    
    @index.setter
    def index(self, new: int) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def clear(self) -> None:
        """Simply clears the screen. No ansi, no complexity. Simple and disconnected."""
        ...
    
    def space(self) -> None:
        """Simply print a space in the terminal."""
        ...
    
    def print(
        self,
        *values: object,
        sep: Optional[str] = " ",
        end: Optional[str] = "\n",
        color: bool = False,
        clear_screen: bool = False,
        prefix: str = "",
        suffix: str = "",
    ) -> None:
        """
        Print values to the terminal with optional formatting.

        Supports:
        - Color tags (like $red)
        - Prefix/suffix
        - Screen clearing
        """
        ...
    
    def render(
        self,
        sep: Optional[str] = " ",
        end: Optional[str] = "\n",
        flush: bool = False,
        color: bool = False,
        clear_screen: ClearScreenArg = False,
        prefix: str = "",
        suffix: str = "",
    ) -> None:
        """Render this to the terminal."""
        ...