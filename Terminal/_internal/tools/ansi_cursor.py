from typing import Literal

__all__ = ("AnsiCursor",)

class AnsiCursor:
    @classmethod
    def cursor_to(cls, row: int, col: int) -> str:
        return f"\033[{row};{col}H"
    
    @classmethod
    def cursor_up(cls, n: int = 1) -> str:
        return f"\033[{n}A"
    
    @classmethod
    def cursor_down(cls, n: int = 1) -> str:
        return f"\033[{n}B"
    
    @classmethod
    def cursor_forward(cls, n: int = 1) -> str:
        return f"\033[{n}C"
    
    @classmethod
    def cursor_backward(cls, n: int = 1) -> str:
        return f"\033[{n}D"
    
    @classmethod
    def cursor_next_line(cls, n: int = 1) -> str:
        return f"\033[{n}E"
    
    @classmethod
    def cursor_prev_line(cls, n: int = 1) -> str:
        return f"\033[{n}F"
    
    @classmethod
    def save_cursor(cls) -> str:
        return "\033[s"
    
    @classmethod
    def restore_cursor(cls) -> str:
        return "\033[u"
    
    @classmethod
    def erase_line(cls, n: Literal[0, 1, 2] = 2) -> str:
        return f"\033[{n}K"
    
    @classmethod
    def erase_screen(cls) -> str:
        return "\033[2J"
    
    @classmethod
    def erase_home(cls) -> str:
        return "\033[H"
    
    @classmethod
    def show_cursor(cls) -> str:
        return "\033[?25h"
    
    @classmethod
    def hide_cursor(cls) -> str:
        return "\033[?25l"