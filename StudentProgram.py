import StudentClass as s

id1 = input("Enter Student ID: ")
n1 = input("Enter Name: ")
dob1 = input("Enter Your DOB: ")
cla1 = input("Enter Your Classification: F,Soph,Jr,Sr: ")

Student = s.Student(id1, n1, dob1, cla1)

print(f"Student {n1} with ID {id1} is a '{cla1}' class student")

"""
if cla1 == "F":
    register = "11/10 thru 11/12 "
elif cla1 == "Jr":
    register = "11/4 thru 11/6"
elif cla1 == "Soph":
    register = "11/7 thru 11/9"
elif cla1 == "Sr":
    register = "11/1 thru 11/3"
"""
print(f"Student can register during : {Student.register(cla1)}")
