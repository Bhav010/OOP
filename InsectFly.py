import InsectClass as i

wings = 2
# legs = 4

# taking user input for choice of bug
n1 = input(f"enter the name of bug: mosquito or housefly? ")
if n1 == "mosquito":
    legs = 4
else:
    legs = 6

# create object of class
bug = i.Insect(n1, wings, legs)

bug.calc_flight()

print(f"The {n1} has {legs} legs and can fly upto {bug.get_flight()} miles")

# mosquito = i.Insect()
# housefly = i.Insect()

# mosquito.calc_flight()
# housefly.calc_flight()

# print(f"The mosquito can fly upto {mosquito.get_flight()} miles")
# print(f"The housefly can fly upto {housefly.get_flight()} miles")
