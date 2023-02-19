import random
from datetime import date


class Student:
    def __init__(self, id, n, dob, cla):
        self.studentid = id
        self.name = n
        self.date = dob
        self.classification = cla

    def cal_age(self, dob):
        today = date.today()
        self.age = today - dob
        return self.age

    def get_name(self):
        return self.name

    def register(self, cla):
        if cla == "F":
            self.register1 = "11/10 thru 11/12 "
        elif cla == "Jr":
            self.register1 = "11/4 thru 11/6"
        elif cla == "Soph":
            self.register1 = "11/7 thru 11/9"
        elif cla == "Sr":
            self.register1 = "11/1 thru 11/3"
        return self.register1
