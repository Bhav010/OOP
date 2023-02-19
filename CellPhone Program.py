import CellPhoneClass as c  # import class

"""
#hard-coded values of attributes
manufact = "Samsung"
model = "S42"
retail_price = "$800"
"""

# change hard-coded attributes to user input
manufact = input(f"Enter the Manufacturer")
model = input(f"Enter the Model")
retail_price = input(f"Enter the Price")
# creat class object
Phone1 = c.CellPhone(manufact, model, retail_price)

# use class object to call methods from class

print(
    f"The manufacturer is: {Phone1.get_manufact()}, model is: {Phone1.get_model()}, Retail price is: {Phone1.get_retail_price()}"
)
