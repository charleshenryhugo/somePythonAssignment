class Person:
    family_name = ""
    age = 0
    given_name = ""

    def __init__(self, S, M, A):
        self.family_name = S
        self.given_name = M
        self.age = A

    def __lt__(self, other):
        if self.family_name != other.family_name:
            return self.family_name < other.family_name
        elif self.age != other.age:
            return self.age < other.age
        else:
            return self.given_name < other.given_name