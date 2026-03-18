
totalBill = input("Welcome to the Tip Calculator\nWhat was the Total Bill?")

tip = input("How much of a tip would you like to enter? 10%, 12%, 15%, or more?")

people = input("How many people to split the bill?")

tb = float(totalBill)
t = int(tip)
p = int(people)

percent = (t/100)*tb
total = percent/p

print(f"Each person should pay: {total}")