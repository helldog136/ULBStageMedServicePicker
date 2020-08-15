from servicepicker.problem.constraint import strongConstraint, StrongConstraint

##########
# constraint: StudentAffectedOnlyOnce
# type: strong
##########

@strongConstraint
class StudentAffectedOnlyOnce(StrongConstraint):
    def computeConstraint(self, problem):
        # sum_i xij = M[j]
        res = []
        for i in range(len(problem.Students)):
            res.append([])
        for i in range(len(problem.Students)):
            for j in range(len(problem.Locations)):
                res[i].append((1, problem.prettyPrintVar("x", i, j)))

        for i, resp in enumerate(res):
            self.addTerm(resp, "=", 1)

    def checkValidity(self, X, L, M, S, P): # not implemented, will crash
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
        for j in range(len(problem.Max_Places)):
            res.append([])
        for j in range(len(problem.Locations)):
            for i in range(len(problem.Students)):
                res[j].append((1, problem.prettyPrintVar("x", i, j)))

        for j, resp in enumerate(res):
            self.addTerm(resp, "<=", problem.Max_Places[j])

    def checkValidity(self, X, L, M, S, P):
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
class AtLeastOneStudentPerPlace(StrongConstraint):
    def computeConstraint(self, problem):
        # sum_i xij >= 1
        res = []
        for j in range(len(problem.Max_Places)):
            res.append([])
        for j in range(len(problem.Locations)):
            for i in range(len(problem.Students)):
                res[j].append((1, problem.prettyPrintVar("x", i, j)))

        for j, resp in enumerate(res):
            self.addTerm(resp, ">=", 1)

    def checkValidity(self, X, L, M, S, P):
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
        # sum_i xij >= 1
        res = []
        for j in range(len(problem.Locations)):
            for i in range(len(problem.Students)):
                if problem.Preferences[i][j] == "X":
                    res.append([(1, problem.prettyPrintVar("x", i, j))])

        for i, resp in enumerate(res):
            self.addTerm(resp, "=", 0)

    def checkValidity(self, X, L, M, S, P):
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
