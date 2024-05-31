print("The Love Calculator is calculating your score...")

name1 = input("Enter the first name: ").lower()
name2 = input("Enter the second name: ").lower()

count1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
count2 = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
count3 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
count4 = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

count_sum = (count3 + count4) * 10 + (count1 + count2)

if count_sum < 10 or count_sum > 90:
    print(f"Your score is {count_sum}, you go together like coke and mentos")
elif 40 <= count_sum <= 50:
    print(f"Your score is {count_sum}, you are alright together")
else:
    print(f"Your score is {count_sum}")
