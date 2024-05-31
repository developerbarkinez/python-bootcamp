year = int(input())

if year % 4 == 0:
    print("Artık yıl adayıdır.")
    if year % 100 == 0 and year % 400 == 0:
        print("100/400 ile bölünüyor, artık yıl olduğu kesindir.")
    elif year % 100 == 0 and year % 400 != 0:
        print("100 ile bölünür. 400 ile tam bölünmez, artık yıl değil.")
    else:
        print("4 ile bölünür ve 100 ile bölünmez, bu yüzden artık yıldır.")
else:
    print("Artık yıl değil.")
