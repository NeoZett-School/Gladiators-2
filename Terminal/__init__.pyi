from typing import Tuple, Type, Optional, Union, Literal, overload
from ._internal import (
    Utils as _Utils, 
    AnsiColor as _AnsiColor,
    AnsiCursor as _AnsiCursor,
    Builder as _Builder, 
    FileSystem as _FileSystem, 
    Terminal as _Terminal, 
    Mode as _Mode,
    Pages as _Pages
)
from ._internal.core import History as _History, Manager, ClearScreenArg

Mode: Type[_Mode]
Terminal: Type[_Terminal]
Simple: Type[_Terminal.Simple]
History: Type[_History]
Builder: Type[_Builder]
FileSystem: Type[_FileSystem]
Utils: Type[_Utils]
AnsiColor: Type[_AnsiColor]
AnsiCursor: Type[_AnsiCursor]
Pages: Type[_Pages]

manager: Manager

IOString: Type[_Terminal.IOString]
AnimatedString: Type[_Terminal.AnimatedString]
ProgressBar: Type[_Terminal.ProgressBar]

# --------------------
# Public API Functions
# --------------------

def terminal_init() -> None: ...
def terminal_deinit() -> None: ...

def print(
    *values: object,
    sep: Optional[str] = " ",
    end: Optional[str] = "\n",
    flush: bool = False,
    color: bool = False,
    clear_screen: ClearScreenArg = False,
    prefix: str = "",
    suffix: str = "",
) -> None: ...

def input(
    *prompt: object,
    sep: Optional[str] = " ",
    end: Optional[str] = "",
    flush: bool = False,
    color: bool = False,
    clear_screen: ClearScreenArg = False,
    input_text: Optional[str] = "",
    n: int = -1
) -> str: ...

def space() -> None: ...

@overload
def clear(*, ansi: Literal[False] = False) -> None: ...
@overload
def clear(*, ansi: Literal[True], flush: bool = True) -> None: ...

def lookup(tag: str) -> Optional[_Terminal.Color]: ...

def log(
    *msg: object,
    format: str = "[[level]] [msg]",
    level: Literal["INFO", "WARN", "ERROR"] = "INFO",
    time_format: str = "%H:%M",
    color: bool = True
) -> None: ...

def new_env(prefix: Optional[_Terminal.Color] = None, suffix: Optional[_Terminal.Color] = None) -> Manager.Environment: ...

def set_env_mode(mode: Union[_Mode, str] = Mode.SINGLE) -> None: ...

def progress_bar(
    formatted_string: str = "[had]|[need]|[prog]%",
    token: str = "-",
    length: int = 10,
    has: float = 0,
    need: float = 10,
    end: Optional[str] = "",
    color: bool = True
) -> str: ...

def strip_ansi(text: str) -> str: ...
def remove_tags(text: str) -> str: ...
def get_size() -> Tuple[int, int]: ...