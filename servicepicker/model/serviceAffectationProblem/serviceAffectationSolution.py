from typing import List

from servicepicker.model.affectationSolution import AffectationSolution

NOT_AFFECTED = 0
AFFECTED = 1


class ServiceAffectationSolution(AffectationSolution):
    def __init__(self, problem):
        self.problem = problem
        self.solution: List[List[int]] = [[0]]
        self.resetSolutionMatrix()
        self.valid: bool = False
        self.invalidityReason = None

    def resetSolutionMatrix(self) -> None:
        self.solution = []
        for student in range(len(self.problem.Students)):
            self.solution.append([])
            for location in range(len(self.problem.Locations)):
                self.solution[student].append(NOT_AFFECTED)

    def isValid(self) -> bool:
        return self.valid

    def checkValidity(self) -> None:
        self.valid = True
        for strongConstraint in self.problem.strongConstraints:
            validity, reason = strongConstraint.checkValidity(self)
            if validity is False:
                self.valid = False
                self.invalidityReason = reason
                return

    def setSolution(self, value, student_id, location_id):
        self.solution[student_id][location_id] = AFFECTED if value >= 0.5 else NOT_AFFECTED

    def __str__(self):
        res = "SOLUTION: \n"
        for s, student in enumerate(self.problem.Students):
            for l, location in enumerate(self.problem.Locations):
                if self.solution[s][l] == AFFECTED:
                    res += f"{student.name} goes to {location.name}\n"
        return res
