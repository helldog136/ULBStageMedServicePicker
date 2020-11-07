
class Location(object):
    def __init__(self, id: int, name: str, minAssignees: int, maxAssignees: int):
        self.id = id
        self.name = name
        self.minAssignees = minAssignees
        self.maxAssignees = maxAssignees

    def __str__(self):
        return "%s :[%d, %d]".format(self.name, self.minAssignees, self.maxAssignees)
