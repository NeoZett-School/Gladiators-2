from typing import Optional
from .core import Terminal, ClearScreenArg

__all__ = ("Builder",)

class BuilderString:
    def __init__(self, *args: str) -> None:
        self.content = list(args)
        self.index = 0

    @property
    def value(self) -> str:
        return self.content[self.index]
    
    @value.setter
    def value(self, new: str) -> None:
        self.content[self.index] = new
    
    def __str__(self) -> str:
        return self.content[self.index]
    
    def __len__(self) -> int:
        return len(self.content)
    
    def __getitem__(self, index: int) -> str:
        return self.content[index]
    
    def __setitem__(self, index: int, value: str) -> None:
        self.content[index] = value
    
    def _create_space(self) -> None:
        self.content.append("")
    
    def get(self, index: int) -> str:
        return self.content[index]
    
    def clear(self) -> None:
        self.content.clear()

class Builder:
    def __init__(self, value: str = "") -> None:
        self._content = BuilderString(value)
    
    def next(self) -> None:
        self.index += 1
    
    def prev(self) -> None:
        if self.index > 0:
            self.index -= 1
        
    def clear_all(self) -> None:
        self._content.clear()
        self.index = 0
    
    @property
    def value(self) -> str:
        return self._content.value
    
    @value.setter
    def value(self, text: str) -> None:
        self._content.value = text
    
    @property
    def index(self) -> int:
        return self._content.index
    
    @index.setter
    def index(self, new: int) -> None:
        if new < 0:
            raise ValueError("Builder index cannot be negative.")
        self._content.index = new
        while len(self._content) <= new:
            self._content._create_space()
    
    def __str__(self) -> str:
        return self.value
    
    def clear(self) -> None:
        self.value = ""
    
    def space(self) -> None:
        self.value += "\n"
    
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
        if clear_screen: self.clear()
        self.value += Terminal.format(*values, sep=sep, end=end, color=color, prefix=prefix, suffix=suffix)
    
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
        Terminal.print(
            self, 
            sep=sep, 
            end=end, 
            flush=flush,
            color=color,
            clear_screen=clear_screen,
            prefix=prefix,
            suffix=suffix
        )