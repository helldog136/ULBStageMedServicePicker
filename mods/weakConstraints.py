import math

from servicepicker.problem.constraint import *

##########
# constraint:AccountPreferences
# type:weak
##########

@weakConstraint
class AccountPreferences(WeakConstraint):
    def getMinValue(self, problem):
        return 0

    def getMaxValue(self, problem):
        return 0

    def getWeight(self):
        return 10

    def computeConstraint(self, problem):
        for i in range(len(problem.Students)):
            for j in range(len(problem.Preferences[i])):
                weight = problem.Preferences[i][j]
                if weight == "":
                    weight = str(len(problem.Locations))
                if weight != "X":
                    weight = len(problem.Locations) - int(weight)
                    if problem.Old_Affectations:
                        weight = math.floor(weight * (1+problem.Old_Affectations[i]))
                    self.addTerm(-(weight), problem.prettyPrintVar("x", i, j))

