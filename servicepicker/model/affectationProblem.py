from abc import ABCMeta, abstractmethod


class AffectationProblem(metaclass=ABCMeta):

    @abstractmethod
    def getStrongConstraints(self):
        pass

    @abstractmethod
    def getWeakConstraints(self):
        pass

    @abstractmethod
    def getBasicObjectiveFunction(self):
        pass

    @abstractmethod
    def setSolution(self, value, *indexes):
        pass
