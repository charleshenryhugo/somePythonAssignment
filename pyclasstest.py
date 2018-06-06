import datetime

#shokyu
class Mathconst:
    PI = 3.14159
    e = 2.71828

class Hogehoge:
    x = 0

    def __init__(self, x):
        self.x = x

    def plus(self, n):
        return self.x + n

#joukyu
class Complex:
    a = 0
    b = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        if self.b >= 0:
            return str(self.a) + "+" + str(self.b) + "i"
        else:
            return str(self.a) + str(self.b) + "i"


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



d = datetime.datetime(2010, 7, 4, 12, 15, 58)
