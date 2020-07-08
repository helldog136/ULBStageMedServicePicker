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
        for i in range(len(problem.S)):
            for j in range(len(problem.P[i])):
                weight = problem.P[i][j]
                if weight == "":
                    weight = str(len(problem.L))
                weight = len(problem.L) - int(weight)
                self.addTerm(-(weight), problem.prettyPrintVar("x", i, j))

