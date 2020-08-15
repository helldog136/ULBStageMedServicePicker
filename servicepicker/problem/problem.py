import math


def normalize_old_affectations(Old_Affectations):
    Old_Affectations = list(map(lambda x: x if x != "0" else "1", Old_Affectations))
    inted_Old = list(map(int, Old_Affectations))
    res = []
    minV = min(inted_Old)
    maxV = max(inted_Old)
    for v in inted_Old:
        normalized = (v-minV)/(maxV-minV)
        res.append(normalized)
    return res


class Problem(object):
    def __init__(self, Locations, Max_Places, Students, Preferences, _strongConstraints, _weakConstraints, Old_Affectations = None):
        self.sep = "_"
        self.Locations = Locations
        self.Max_Places = Max_Places
        self.Students = Students
        self.Old_Affectations = None
        if Old_Affectations is not None:
            self._original_old = Old_Affectations
            self.Old_Affectations = normalize_old_affectations(Old_Affectations)
        if sum(self.Max_Places) < len(self.Students):
            print(f"Too Many Students ({len(self.Students)}) and too few places ({sum(self.Max_Places)})")
            exit(-1)
        self.Preferences = Preferences
        self.strongConstraints = _strongConstraints
        self.weakConstraints = _weakConstraints
        self.value = None
        problemMatrix = []
        for i in range(len(self.Students)):
            problemMatrix.append([])
            for j in range(len(self.Preferences)):
                problemMatrix[i].append((True, []))
        self.validity = (True, [], [], [], [], problemMatrix)

        # init matrix X for decision variables
        self.X = []
        for i in range(len(self.Students)):
            line1 = []
            for j in range(len(self.Locations)):
                line1.append(0)
            self.X.append(line1)

    def write(self):
        obj = ""
        binr = ""
        for i in range(len(self.X)):
            for j in range(len(self.X[i])):
                obj += self.prettyPrintVar("x", i, j) + " + "
                binr += self.prettyPrintVar("x", i, j) + "\n"

        for c in self.weakConstraints.getConstraints(self):
            print("weak\n------\n" + c + "\n---")
            obj = (obj[:-3] if c[:2] == " -" else obj) + str(c) + \
                  ("" if len(c) == 0 or c[-2:] == "+ " else " + ")
        obj = obj[:-2]

        cst = ""
        for c in self.strongConstraints.getConstraints(self):
            print("strong\n------\n" + c + "\n---")
            cst += str(c) + ("" if len(c) == 0 or c[-1] == "\n" else "\n")

        res = "Minimize\n"
        res += obj
        res += "\n"
        res += "Subject To\n"
        res += cst
        res += "Binary\n"
        res += binr
        res += "End"

        print(res)
        return res

    def prettyPrintVar(self, var, i, j):
        return var + self.sep + str(i) + self.sep + str(j)

    def resetSolution(self):
        for i in range(len(self.X)):
            for j in range(len(self.X[i])):
                self.X[i][j] = 0

    def setSolution(self, sol):
        # wipe data in X
        self.resetSolution()

        print(sol)

        for t in sol["solution"]:
            self._setSol(*t)
        self.value = sol["value"]

    def _setSol(self, var, val):
        _, i, j = var.split(self.sep)
        i = int(i)
        j = int(j)
        print(f"Setting {self.Students[i]} to {self.Locations[j]} ({val})")
        self.X[i][j] = int(val)

    def displaySolution(self):
        print(self.getSolutionAsStr())

    def getSolutionAsStr(self):
        res = ""
        for i in range(len(self.X)):
            for j in range(len(self.X[i])):
                if self.X[i][j] == 1:
                    Affectation = f"{self.Students[i]} va à {self.Locations[j]}. "
                    Preference = f"Il/Elle y avait mis une préférence de {self.Preferences[i][j]} " if self.Preferences[i][j] != "" else "Ce n'était pas une de ses préférences... Désolé... "
                    RemarkOld = ""
                    if self.Old_Affectations:
                        if self._original_old[i] == "0":
                            RemarkOld = "Il/Elle ne faisait pas partie du choix la fois précédente"
                        else:
                            RemarkOld = f"Sa précédente affectation était son {self._original_old[i]}{'eme' if self._original_old[i] != '1' else 'er '} choix."
                    res += Affectation + Preference + RemarkOld + "\n"
        return res

    def getSolutionAsCSV(self):
        res = "Students\\Services,"
        res += ",".join(self.Locations)
        res += "\n"
        for i, s in enumerate(self.Students):
            res += s + ","
            for j, xij in enumerate(self.X[i]):
                if xij != 0:
                    res += self.Preferences[i][j] if self.Preferences[i][j] != "" else str(len(self.Locations))
                res += ","
            res = res[:-1] + "\n"
        return res
