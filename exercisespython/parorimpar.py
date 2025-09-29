print ("Welcome to the python pizza deliveries! ")

size = input("What size do you want? Small, Medium or Large? ")
if size == "Small":
    bill = 15
elif size == "Medium":
    bill = 20
else:
    bill = 25

peperoni = input("Do you want pepperoni? Y or N ")
if peperoni == "Y":
    if size == "Small":
        bill += 2
    elif size == "Medium" or size == "Large":
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")


