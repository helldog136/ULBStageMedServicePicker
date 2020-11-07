from pulp import LpProblem, LpMinimize

from servicepicker.model.affectationProblem import AffectationProblem


class Solver():
    def solve(self, problem: AffectationProblem):
        # Create the model
        model = LpProblem(name="affectation-problem", sense=LpMinimize)

        obj = problem.getBasicObjectiveFunction()

        for weakConstraint in problem.getWeakConstraints():
            obj += weakConstraint

        model += obj

        for strongConstraint in problem.getStrongConstraints():
            model += strongConstraint

        print(model)

        model.solve()

        print(model)

        for var in model.variables():
            _, stud, loc = var.name.split("_")
            stud, loc = int(stud), int(loc)
            problem.setSolution(var.value(), stud, loc)
            print(f"{var.name}: {var.value()}")
