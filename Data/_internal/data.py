"""A flexible data container class that behaves like both a dictionary and an object with attributes."""

from typing import (
    Set, List, Dict, Any, Optional, Type, TypeVar, Generic, 
    Literal, overload, KeysView, ValuesView, ItemsView
)
from .meta import DataMeta

V = TypeVar("V")
DictSchema = Dict[str, V]

class Data(Generic[V], metaclass=DataMeta):
    """A flexible data container class that behaves like both a dictionary and an object with attributes."""
    _meta: Dict[str, Any] = {}
    _banned_attributes: Set[str] = {"_banned_attributes", "_meta", "content"}

    def __init__(self, value: Optional[DictSchema] = None, /, **kwargs: Any) -> None:
        """Initializes the Data object with optional dictionary content and keyword arguments."""
        instance_kwargs = dict()
        instance_kwargs.update(value or {})
        instance_kwargs.update(kwargs) # Overwrite with instance-level arguments

        object.__setattr__(self, "content", instance_kwargs)
        self.__raise_typing_error__()
    
    @property
    def meta(self) -> Dict[str, Any]:
        """Allocate and retrieve relevant metadata for the Data object."""
        this_meta = object.__getattribute__(self, "_meta")
        has_meta = bool(this_meta and len(this_meta) > 0)
        other_meta = self.__get_content__().get("_meta", {})
        return this_meta if has_meta else other_meta
    
    def __get_incorrect_typing__(self) -> List[str]:
        return list(k for k, v in self.__get_content__().get("__annotations__", {}).items() if not isinstance(getattr(self, k), v))
    
    def __raise_typing_error__(self) -> None:
        incorrect = self.__get_incorrect_typing__()
        if incorrect:
            raise TypeError(f"Incorrect typing for fields: {', '.join(incorrect)}")
    
    def __get_content__(self) -> DictSchema:
        return object.__getattribute__(self, "content")
    
    def copy(self) -> "Data[V]":
        """Creates a shallow copy of the Data object."""
        return self.__class__(self.__get_content__().copy())
    
    @classmethod
    def from_dict(cls: Type["Data[V]"], data: DictSchema) -> "Data[V]":
        """Creates a Data object from a dictionary."""
        return cls(data)
    
    def to_dict(self) -> DictSchema:
        """Converts the Data object to a standard dictionary."""
        return dict(self.__get_content__())
    
    def keys(self) -> KeysView[str]:
        """Return a set-like object providing a view on the data's keys."""
        return self.__get_content__().keys()
    def values(self) -> ValuesView[V]:
        """Return a set-like object providing a view on the data's values."""
        return self.__get_content__().values()
    def items(self) -> ItemsView[str, V]:
        """Return a set-like object providing a view on the data's items."""
        return self.__get_content__().items()
    
    @overload
    def get(self, key: str, default: Literal[None] = None) -> Optional[V]: ...
    @overload
    def get(self, key: str, default: V) -> V: ...
    def get(self, key: str, default: Optional[V] = None) -> Optional[V]:
        """Return the value for key if key is in the dictionary, else default."""
        return self.__get_content__().get(key, default)
    
    @overload
    def setdefault(self, key: str, default: Literal[None] = None) -> Optional[V]: ...
    @overload
    def setdefault(self, key: str, default: V) -> V: ...
    def setdefault(self, key: str, default: Optional[V] = None) -> Optional[V]:
        result = self.__get_content__().setdefault(key, default)
        self.__raise_typing_error__()
        return result
    
    @overload
    def pop(self, key: str, default: Literal[None] = None) -> Optional[V]: ...
    @overload
    def pop(self, key: str, default: V) -> V: ...
    def pop(self, key: str, default: Optional[V] = None) -> Optional[V]:
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

        If the key is not found, return the default if given; otherwise,
        raise a KeyError.
        """
        return self.__get_content__().pop(key, default)
    
    def update(self, data: DictSchema) -> None:
        self.__get_content__().update(data)
        self.__raise_typing_error__()
    
    def clear(self) -> None:
        self.__get_content__().clear()
    
    def __call__(self, key: str, /, *args: Any, **kwargs: Any) -> Any:
        """Calls a callable stored in the data with the given key, passing any additional arguments."""
        return self.__get_content__()[key](*args, **kwargs)
    
    def __getattribute__(self, name: str) -> Any:
        # Allow internal access first
        if name in object.__getattribute__(self, "_banned_attributes"):
            raise AttributeError(f"'{name}' is a reserved attribute and cannot be set.")
        # Try to get real attribute
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        # Fallback to content
        content = object.__getattribute__(self, "content")
        if name in content:
            return content[name]
        raise AttributeError(f"'Data' object has no attribute '{name}'")
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name in object.__getattribute__(self, "_banned_attributes"):
            raise AttributeError(f"'{name}' is a reserved attribute and cannot be set.")
        content = object.__getattribute__(self, "content")
        content[name] = value
        self.__raise_typing_error__()
    
    def __getitem__(self, key: str) -> V:
        return self.__get_content__()[key]
    def __setitem__(self, key: str, value: V) -> None:
        self.__get_content__()[key] = value
        self.__raise_typing_error__()
    def __delitem__(self, key: str) -> None:
        del self.__get_content__()[key]
    def __contains__(self, key: str) -> bool:
        return key in self.__get_content__()
    def __iter__(self):
        return iter(self.__get_content__())
    def __len__(self) -> int:
        return len(self.__get_content__())
    def __repr__(self) -> str:
        return f"Data({self.__get_content__()})"
    def __str__(self) -> str:
        return str(self.__get_content__())