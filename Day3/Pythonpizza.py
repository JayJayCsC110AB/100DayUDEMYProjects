print("Welcome to Python Pizza Deliveries!")
Size = input("What size do you want? S, M, or L ")
Pepporoni = input("Do you want pepporoni on your pizza? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


bill = 0
if Size == "S":
    bill += 15
elif Size == "M":
    bill += 20
elif Size == "L":
    bill += 25
else:
    print("You typed the wrong input")

if Pepporoni == "Y":
    if Size == "S":
        bill += 2
    else: 
        bill +=3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")