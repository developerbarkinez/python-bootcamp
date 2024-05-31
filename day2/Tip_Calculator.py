print("Welcome to the tip calculator!")
bill=input("What was the total bill?\n")
tip=input("How much tip would you like to give? 10 12 15\n")
split=input("How many people to split the bill?\n")


x=float(bill)
y=int(tip)
z=int(split)


pay=(x*(y/100)+x)/z

final_amount=(round(pay,2))

print(f"Each person should pay ${final_amount}")