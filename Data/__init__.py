from typing import Type
from ._internal import Data, dataclass
import sys

class Module:
    Data: Type[Data]
    dataclass: Type[dataclass]
    def __getattr__(self, name: str):
        if name == "Data":
            return Data
        if name == "dataclass":
            return dataclass
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

__all__ = ('Data', 'dataclass')
sys.modules[__name__] = Module()