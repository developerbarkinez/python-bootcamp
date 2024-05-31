height = float(input("Height in meters: "))
weight = int(input("Weight in kilograms: "))

bmi = weight / (height * height)
x = round(bmi, 2)

if x < 18.5:
    print(f"{x} Underweight")
elif x >= 18.5 and x < 25:
    print(f"{x} Normal weight")
elif x >= 25 and x < 30:
    print(f"{x} Slightly overweight")
elif x >= 30 and x < 35:
    print(f"{x} Obese")
else:
    print(f"{x} Clinically obese")
