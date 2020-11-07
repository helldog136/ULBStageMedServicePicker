from typing import List

from servicepicker.model.constraint import StrongConstraint

_strongConstraints: List[StrongConstraint] = []


def getStrongConstraints():
    global _strongConstraints
    return _strongConstraints


def strongConstraint(const):
    global _strongConstraints
    _strongConstraints.append(const())


##########
# constraint: StudentAffectedOnlyOnce
# type: strong
##########

@strongConstraint
class StudentAffectedOnlyOnce(StrongConstraint):
    def computeConstraint(self, problem):
        # sum_i xij = M[j]
        res = []
        for s, student in enumerate(problem.Students):
            const = None
            for l, location in enumerate(problem.Locations):
                if const is None:
                    const = problem.decisionVariables[s][l]
                else:
                    const += problem.decisionVariables[s][l]

            const = (const == 1)
            res.append((const, f"{student.name} affected only once"))
        return res

    def checkValidity(self, problem, solution):  # not implemented, will crash
        res = True
        wrongs = []
        # for k in range(len(M)):
        #     ctr = 0
        #     lst = []
        #     for i in range(len(S)):
        #         for j in range(len(P)):
        #             ctr += X[i][j]
        #             if X[i][j] > 0:
        #                 lst.append((i,j))
        #     res = res and ctr == 1
        #     if not ctr == 1:
        #         for i, j in lst:
        #             wrongs.append((i, j, k, -1))
        return (res, wrongs)


##########
# constraint: NoMoreStudentThanPlaces
# type: strong
##########

@strongConstraint
class NoMoreStudentThanPlaces(StrongConstraint):
    def computeConstraint(self, problem):
        # sum_i xij <= M[j]
        res = []
        for l, location in enumerate(problem.Locations):
            const = None
            for s, student in enumerate(problem.Students):
                if const is None:
                    const = problem.decisionVariables[s][l]
                else:
                    const += problem.decisionVariables[s][l]

            const = (const <= location.maxAssignees)
            res.append((const, f"no more than {location.maxAssignees} students at {location.name}"))
        return res

    def checkValidity(self, problem, solution):
        res = True
        wrongs = []
        # for k in range(len(M)):
        #     ctr = 0
        #     lst = []
        #     for i in range(len(S)):
        #         for j in range(len(P)):
        #             ctr += X[i][j]
        #             if X[i][j] > 0:
        #                 lst.append((i,j))
        #     res = res and ctr == 1
        #     if not ctr == 1:
        #         for i, j in lst:
        #             wrongs.append((i, j, k, -1))
        return (res, wrongs)


##########
# constraint: AtLeastOneStudentPerPlace
# type: strong
##########

@strongConstraint
class EnoughStudentPerPlace(StrongConstraint):
    def computeConstraint(self, problem):
        res = []
        for l, location in enumerate(problem.Locations):
            const = None
            for s, student in enumerate(problem.Students):
                if const is None:
                    const = problem.decisionVariables[s][l]
                else:
                    const += problem.decisionVariables[s][l]

            const = (const >= location.minAssignees)
            res.append((const, f"at least {location.minAssignees} students at {location.name}"))
        return res

    def checkValidity(self, problem, solution):
        res = True
        wrongs = []
        # for k in range(len(M)):
        #     ctr = 0
        #     lst = []
        #     for i in range(len(S)):
        #         for j in range(len(P)):
        #             ctr += X[i][j]
        #             if X[i][j] > 0:
        #                 lst.append((i,j))
        #     res = res and ctr == 1
        #     if not ctr == 1:
        #         for i, j in lst:
        #             wrongs.append((i, j, k, -1))
        return (res, wrongs)


##########
# constraint: AccountVetos (X)
# type: strong
##########

@strongConstraint
class AccountVetos(StrongConstraint):
    def computeConstraint(self, problem):
        res = []
        for s, student in enumerate(problem.Students):
            const = None
            for l, location in enumerate(problem.Locations):
                if student.hasVeto(location.id):
                    if const is None:
                        const = problem.decisionVariables[s][l]
                    else:
                        const += problem.decisionVariables[s][l]
            if const is not None:
                const = (const == 0)
                res.append((const, f"{student.name} vetos"))
        return res

    def checkValidity(self, problem, solution):
        res = True
        wrongs = []
        # for k in range(len(M)):
        #     ctr = 0
        #     lst = []
        #     for i in range(len(S)):
        #         for j in range(len(P)):
        #             ctr += X[i][j]
        #             if X[i][j] > 0:
        #                 lst.append((i,j))
        #     res = res and ctr == 1
        #     if not ctr == 1:
        #         for i, j in lst:
        #             wrongs.append((i, j, k, -1))
        return (res, wrongs)
