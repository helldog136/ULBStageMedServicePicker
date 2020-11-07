import math

from servicepicker.model.constraint import WeakConstraint

weakConstraints = []


def getWeakConstraints():
    global weakConstraints
    return weakConstraints


def weakConstraint(const):
    global weakConstraints
    weakConstraints.append(const())


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
        res = []
        for s,student in enumerate(problem.Students):
            weights = None
            for l, location in enumerate(problem.Locations):
                weight = student.getPreference(location.id) * problem.decisionVariables[s][l]
                if weights is None:
                    weights = weight
                else:
                    weights += weight
            res.append(weights)
        return res
