"""
The Terminal provides all features you will ever need when building your CLI applications.
"""

from typing import Tuple, Optional, Literal, Union

from . import core
from ._internal import (
    Utils, 
    AnsiColor, 
    AnsiCursor, 
    Builder, 
    FileSystem, 
    Terminal, 
    Mode, 
    Pages
)
from ._internal.core import History, Manager, ClearScreenArg
from . import ansi, builder, pages, files, tools
import sys

class Module:
    @staticmethod
    def terminal_init() -> None:
        Terminal.init()

    @staticmethod
    def terminal_deinit() -> None:
        Terminal.deinit()
    
    @staticmethod
    def print(
        *values: object,
        sep: Optional[str] = " ",
        end: Optional[str] = "\n",
        flush: bool = False,
        color: bool = False,
        clear_screen: ClearScreenArg = False,
        prefix: str = "",
        suffix: str = "",
    ) -> None: 
        Terminal.print(
            *values, 
            sep=sep, 
            end=end, 
            flush=flush, 
            color=color, 
            clear_screen=clear_screen, 
            prefix=prefix,
            suffix=suffix
        )
    
    @staticmethod
    def input(
        *prompt: object,
        sep: Optional[str] = " ",
        end: Optional[str] = "",
        flush: bool = False,
        color: bool = False,
        clear_screen: ClearScreenArg = False,
        input_text: Optional[str] = "",
        n: int = -1
    ) -> str:
        return Terminal.input(
            *prompt, 
            sep=sep, 
            end=end, 
            flush=flush, 
            color=color, 
            clear_screen=clear_screen, 
            input_text=input_text, 
            n=n
        )
    
    def space() -> None:
        Terminal.space()
    
    @staticmethod
    def clear(*, ansi: bool = False, flush: bool = True) -> None:
        Terminal.clear(ansi=ansi,flush=flush)
    
    @staticmethod
    def lookup(tag: str) -> Optional[Terminal.Color]:
        return Terminal.lookup(tag)
    
    @staticmethod
    def log(
        *msg: object, format: str = "[[level]] [msg]", level: Literal["INFO", "WARN", "ERROR"] = "INFO", time_format: str = "%H:%M", color: bool = True
    ) -> None:
        Terminal.log(*msg, format=format, level=level, time_format=time_format, color=color)
    
    @staticmethod
    def new_env(prefix: Optional[Terminal.Color] = None, suffix: Optional[Terminal.Color] = None) -> Manager.Environment:
        return Terminal.new_env(prefix, suffix)
    
    @staticmethod
    def set_env_mode(mode: Union[Mode, str] = Mode.SINGLE) -> None:
        Terminal.set_env_mode(mode)
    
    @staticmethod
    def progress_bar(
        formatted_string: str = "[had]|[need]|[prog]%",
        token: str = "-", length: int = 10,
        has: float = 0, need: float = 10,
        end: Optional[str] = "", color: bool = True
    ) -> str:
        return Terminal.progress_bar(
            formatted_string, 
            token, length,
            has, need, 
            end, color 
        )

    @staticmethod
    def strip_ansi(text: str) -> str:
        return Terminal.strip_ansi(text)
    
    @staticmethod
    def remove_tags(text: str) -> str:
        return Terminal.remove_tags(text)

    @staticmethod
    def get_size() -> Tuple[int, int]:
        return Terminal.get_size()

    Mode = Mode
    Terminal = Terminal
    Simple = Terminal.Simple
    History = History
    Builder = Builder
    FileSystem = FileSystem
    Utils = Utils
    AnsiColor = AnsiColor
    AnsiCursor = AnsiCursor
    Pages = Pages
    manager = Terminal.manager

    IOString = Terminal.IOString
    AnimatedString = Terminal.AnimatedString
    ProgressBar = Terminal.ProgressBar

    pages = pages
    ansi = ansi
    core = core
    files = files
    builder = builder
    tools = tools

    terminal_init()

    @classmethod
    def get_module(cls):
        return cls

sys.modules[__name__] = Module