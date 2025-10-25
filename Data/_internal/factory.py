from typing import TypeVar, Any
from .data import Data

T = TypeVar("T", bound=Data)

class _Dataclass(Data):
    def __init__(self, cls: T, /, **kwargs: Any) -> None:
        self.__annotations__.update(cls.__annotations__)
        kwargs.update(cls.__dict__)
        super().__init__(kwargs)
    def __repr__(self) -> str:
        fields = ', '.join(f"{key}={value!r}" for key, value in self.items() if key.startswith("_") is False and not callable(value))
        return f"{self.__class__.__name__}({fields})"
    def __str__(self) -> str:
        return self.__repr__()

def dataclass(cls: T, /) -> T:
    """
    Converts a standard class into a Data-like class.

    For correct typing, you must inherit from Data in the class definition.
    """
    def wrapper(**kwargs: Any) -> T:
        return type(cls.__name__, (_Dataclass,), dict(cls.__dict__))(cls, **kwargs)
    return wrapper