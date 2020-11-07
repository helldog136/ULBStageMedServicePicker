from typing import List

from servicepicker.model.serviceAffectationProblem.constraints.strongConstraints import getStrongConstraints
from servicepicker.model.serviceAffectationProblem.constraints.weakConstraints import getWeakConstraints
from servicepicker.model.serviceAffectationProblem.location import Location
from servicepicker.model.affectationProblem import AffectationProblem
from servicepicker.model.serviceAffectationProblem.serviceAffectationSolution import ServiceAffectationSolution
from servicepicker.model.serviceAffectationProblem.student import Student

from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, const


def normalize_old_affectations(Old_Affectations):
    Old_Affectations = list(map(lambda x: x if x != "0" else "1", Old_Affectations))
    inted_Old = list(map(int, Old_Affectations))
    res = []
    minV = min(inted_Old)
    maxV = max(inted_Old)
    for v in inted_Old:
        normalized = (v - minV) / (maxV - minV)
        res.append(normalized)
    return res


class ServiceAffectationProblem(AffectationProblem):
    def setSolution(self, value, student_id, location_id, *_):
        self.solution.setSolution(value, student_id, location_id)

    def __init__(self, _Locations: List[Location], _Students: List[Student]):
        self.Locations = _Locations
        self.Students = _Students
        maxNbPlaces = sum([location.maxAssignees for location in self.Locations])
        assert maxNbPlaces >= len(self.Students), \
            f"Too Many Students ({len(self.Students)}) " \
            f"and too few places ({maxNbPlaces}) "
        minNbPlaces = sum([location.minAssignees for location in self.Locations])
        assert minNbPlaces <= len(self.Students), \
            f"Too Few Students ({len(self.Students)}) " \
            f"for the minimal number of places ({minNbPlaces}) "
        self.strongConstraints = getStrongConstraints()
        self.weakConstraints = getWeakConstraints()

        self.decisionVariables = None
        self.initDecisionVariables()

        self.solution: ServiceAffectationSolution = ServiceAffectationSolution(self)

    def getStrongConstraints(self):
        res = []
        for strongConstraint in self.strongConstraints:
            res.extend(strongConstraint.computeConstraint(self))
        return res

    def getWeakConstraints(self):
        res = []
        for weakConstraint in self.weakConstraints:
            res.extend(weakConstraint.computeConstraint(self))
        return res

    def getBasicObjectiveFunction(self):
        res = None
        for s, student in enumerate(self.Students):
            for l, location in enumerate(self.Locations):
                if res is None:
                    res = self.decisionVariables[s][l]
                else:
                    res += self.decisionVariables[s][l]
        return res

    def initDecisionVariables(self):
        self.decisionVariables = []
        for s, student in enumerate(self.Students):
            self.decisionVariables.append([])
            for location in self.Locations:
                self.decisionVariables[s].append(
                    LpVariable(name=f"x_{student.id}_{location.id}", lowBound=0, upBound=1, cat=const.LpBinary))
