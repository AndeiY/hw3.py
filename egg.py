a = int(1)
while True:
    if a % 2 == 1 and a % 3 == 1 and a % 4 == 1 and a % 5 == 1 and a % 6 == 1 and a % 7 == 0:
        print(a)
        break
    else:
        a += 1
