import random


# With user inputs
class Insect:
    def __init__(self, n, w, l):
        self.wings = w
        self.legs = l
        self.name = n
        self.flight = 0

    def calc_flight(self):
        self.flight = random.randint(1, 10)

    def get_flight(self):
        return self.flight

    def get_name(self):
        return self.name


# With hard-coded values
"""
class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.name = ""
        self.flight = 0

    def calc_flight(self):
        self.flight = random.randint(1, 10)

    def get_flight(self):
        return self.flight

    def get_name(self):
        return self.name
"""
