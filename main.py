#!/usr/bin/env python3
import sys
import servicepicker.model.constraint as constraint
import os

from servicepicker.model.serviceAffectationProblem.location import Location
from servicepicker.model.serviceAffectationProblem.serviceAffectationProblem import ServiceAffectationProblem
from servicepicker.model.serviceAffectationProblem.student import Student
from servicepicker.model.solver import Solver

if __name__ == "__main__":
    studs = []
    studs.append(Student(0, "John Doe", {0: 1, 1: 4, 2: 2, 3: 3}, priority=0.75))
    studs.append(Student(1, "Jane Doe", {0: 4, 1: 2, 2: 1, 3: 3}))
    studs.append(Student(2, "Jon Done", {0: 2, 1: 3, 2: 4, 3: 1}, vetos=[2], priority=1.5))

    locs = []
    locs.append(Location(0, "A", 0, 2))
    locs.append(Location(1, "B", 1, 2))
    locs.append(Location(2, "C", 1, 1))
    locs.append(Location(3, "D", 0, 1))

    problem = ServiceAffectationProblem(locs, studs)

    solver = Solver()

    solver.solve(problem)

    print(problem.solution)
