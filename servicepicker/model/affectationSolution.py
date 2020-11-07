from abc import ABCMeta, abstractmethod


class AffectationSolution(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def isValid(cls) -> bool:
        pass
