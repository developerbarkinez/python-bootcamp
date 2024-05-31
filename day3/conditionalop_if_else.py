print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?\n"))

bill = 0
x_bill = int(bill)
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age in number?\n"))
    if (age < 12):
        bill = 5
        print(f"You must pay {bill}$")
    elif age >= 12 and age <= 18:
        bill = 7
        print(f"You must pay {bill}$")
    elif age>18 and age<45:
        bill = 12
        print(f"You must pay {bill}$")
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"You must pay {bill}$.It's Free")
    photo = input("Want Photos? Yes Or No\n")
    if photo == "Yes":
        bill += 3
        print(f"Your total bill is ${bill}")
    else:
        print(f"Your total bill is ${bill}")


else:
    print("Sorry,you have to grow taller before you can ride.")
