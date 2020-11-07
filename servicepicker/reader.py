from servicepicker.model import ServiceAffectationProblem, getStrongConstraints, getWeakConstraints


def parse(filename):
    services = []
    max_places = []
    students = []
    student_preferences = []
    with open(filename, 'r', encoding='utf-8') as inputf:
        firstLine = True
        secondLine = True
        for line in inputf:
            lnSplitted = line.strip().split(",")
            if firstLine:
                firstLine = False
                services = lnSplitted[1:]
            elif secondLine:
                secondLine = False
                max_places.extend(int(n) for n in lnSplitted[1:])
            else:
                student = lnSplitted[0]
                studentChoices = lnSplitted[1:]
                students.append(student)
                student_preferences.append(studentChoices)
    print(services)
    print(max_places)
    print(students)
    print(student_preferences)
    print(f"Creating problem with {len(students)} Students with {sum(max_places)} places.")
    return ServiceAffectationProblem(services, max_places, students, student_preferences, getStrongConstraints(), getWeakConstraints())

def parse_with_old_result(filename):
    services = []
    max_places = []
    students = []
    student_preferences = []
    old_result = []
    with open(filename, 'r', encoding='utf-8') as inputf:
        firstLine = True
        secondLine = True
        for line in inputf:
            lnSplitted = line.strip().split(",")
            if firstLine:
                firstLine = False
                services = lnSplitted[2:]
            elif secondLine:
                secondLine = False
                max_places.extend(int(n) for n in lnSplitted[2:])
            else:
                student = lnSplitted[0]
                studentChoices = lnSplitted[2:]
                old_res = lnSplitted[1]
                old_res = old_res if old_res != "" else "0"
                students.append(student)
                student_preferences.append(studentChoices)
                old_result.append(old_res)
    print(services)
    print(max_places)
    print(students)
    print(student_preferences)
    print(old_result)
    print(f"Creating problem with {len(students)} Students with {sum(max_places)} places.")
    return ServiceAffectationProblem(services, max_places, students, student_preferences, getStrongConstraints(), getWeakConstraints(), old_result)

if __name__ == "__main__":
    print(parse("input.csv").write())
    print(parse_with_old_result("input2.csv").write())
