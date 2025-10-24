from typing import Dict, Optional, Self
from enum import Enum, auto
from constants import DIFFICULTY_DATA

class Difficulty(Enum):
    EASY = auto()
    NORMAL = auto()
    HARD = auto()

    @property
    def data(self) -> Dict:
        return DIFFICULTY_DATA[self.name]

    def title(self) -> str:
        return self.name.capitalize()
    
    @classmethod
    def get(cls, name: str) -> Optional[Self]:
        return cls.__members__.get(name.upper())