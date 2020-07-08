from filereader.problem import Problem, getStrongConstraints, getWeakConstraints


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
    return Problem(services, max_places, students, student_preferences, getStrongConstraints(), getWeakConstraints())

if __name__ == "__main__":
    print(parse("input.csv").write())