print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # S,M,L
add_pepperoni = input()  # Y OR N
extra_cheese = input()  # Y OR N

price = 0
pepperoni_price = 0
cheese_price = 0


if size == "S" or size == "s":
    price = 15
    if add_pepperoni == 'Y' and extra_cheese == 'Y':
        pepperoni_price = 2
        cheese_price = 1
        price += pepperoni_price
        price += cheese_price
        print(f"You paid {price}$ for {size} pizza.Enjoy!")
    elif add_pepperoni == 'Y' and extra_cheese == 'N':
        pepperoni_price = 2
        price += pepperoni_price
        print(f"You paid {price}$ for {size} pizza.Enjoy!")
    elif add_pepperoni == 'N' and extra_cheese == 'Y':
        cheese_price = 1
        price += cheese_price
        print(f"You paid {price}$ for {size} pizza.Enjoy!")
if size == "M" or size == "m":
    price = 20
    if add_pepperoni == 'Y' and extra_cheese == 'Y':
        pepperoni_price = 3
        cheese_price = 1
        price += pepperoni_price
        price += cheese_price
        print(f"You paid {price}$ for {size} pizza.Enjoy!")
    elif add_pepperoni == 'Y' and extra_cheese == 'N':
        pepperoni_price = 3
        price += pepperoni_price
        print(f"You paid {price}$ for {size} pizza.Enjoy!")
    elif add_pepperoni == 'N' and extra_cheese == 'Y':
        cheese_price = 1
        price += cheese_price
        print(f"You paid {price}$ for {size} pizza.Enjoy!")
if size == "L" or size == "l":
    price = 25
    if add_pepperoni == 'Y' and extra_cheese == 'Y':
        pepperoni_price = 3
        cheese_price = 1
        price += pepperoni_price
        price += cheese_price
        print(f"You paid {price}$ for {size} pizza.Enjoy!")
    elif add_pepperoni == 'Y' and extra_cheese == 'N':
        pepperoni_price = 3
        price += pepperoni_price
        print(f"You paid {price}$ for {size} pizza.Enjoy!")
    elif add_pepperoni == 'N' and extra_cheese == 'Y':
        cheese_price = 1
        price += cheese_price
        print(f"You paid {price}$ for {size} pizza.Enjoy!")
