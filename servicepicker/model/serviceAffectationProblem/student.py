import math
from typing import Dict, List


class Student(object):
    def __init__(self, id: int, name: str, locationPreferences: Dict[int, int], vetos: List[int] = [], priority: float = 1):
        self.id = id
        self.name = name
        self.locationPreferences = locationPreferences
        self.vetos = vetos
        self.priority = priority
        assert self.id >= 0
        assert 0 <= self.priority <= 2

    def getPreference(self, locationId: int) -> float:
        return self.locationPreferences.get(locationId) * self.priority

    def hasVeto(self, locationId: int) -> bool:
        return locationId in self.vetos
