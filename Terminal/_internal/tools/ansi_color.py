from typing import Literal

__all__ = ("AnsiColor",)

class AnsiColor:
    @classmethod
    def reset_all(cls) -> str:
        return "\033[0m"
    
    @classmethod
    def foreground_rgb(cls, r: int, g: int, b: int) -> str:
        return f"\033[38;2;{r};{g};{b}m"
    
    @classmethod
    def background_rgb(cls, r: int, g: int, b: int) -> str:
        return f"\033[48;2;{r};{g};{b}m"
    
    @classmethod
    def style(cls, n: Literal[1, 2, 4]) -> str:
        return f"\033[{n};...m"