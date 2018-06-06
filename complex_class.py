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