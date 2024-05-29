class Primary():
    pass


class Middle():
    pass


class High():
    pass


class School():
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    def getNoStudents(self):
        return self.numberOfStudents

    def setNoOfStudents(self, newNumberOfStudents):
        self.numberOfStudents = newNumberOfStudents

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"


print(f"\n\n##### MIDDLE SCHOOL TEST START #####")
school_middle = School("Stangeland", "Middle", 500)
print(school_middle)
print(school_middle.getName())
print(school_middle.getLevel())
school_middle.setNoOfStudents(12500)
print(school_middle.getNoStudents())

print(f"##### MIDDLE SCHOOL TEST DONE #####\n\n")
# Creating the Primary School Class


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name=name, numberOfStudents=numberOfStudents, level="primary")
        self.pickupPolicy = pickupPolicy

    def getpickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        parentRepr = super().__repr__()
        return f"{parentRepr}. The pickup policy is {self.pickupPolicy}"


print(f"##### PRIMARY SCHOOL TEST START #####")
school_pri = PrimarySchool("Kopervik", 200, "pickup Allowed")
print(school_pri.getName())
print(school_pri.getpickupPolicy())
print(school_pri)

print(f"##### PRIMARY SCHOOL TEST DONE #####\n\n")


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name=name, numberOfStudents=numberOfStudents, level="High")
        self.sportTeams = sportsTeams

    def getSportTeams(self):
        return self.sportTeams

    def __repr__(self):
        parentRepr = super().__repr__()
        return f"{parentRepr} and has the following sport teams: {self.sportTeams}"


print(f"##### HIGH SCHOOL TEST START #####")

school_high = HighSchool("UiS", 12000, ["UiSI", "SiS"])
print(school_high)
print(school_high.getSportTeams())
print(school_high.getLevel())
print(f"##### HIGH SCHOOL TEST DONE #####\n\n")
