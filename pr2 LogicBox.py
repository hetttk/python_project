print("Hello from Logic Box")

while True:
    print("\nChoose: 1=Pattern, 2=Numbers, 3=Exit")
    opt = input("Choice: ")

    if opt == "1":
        n = int(input("How many rows? "))
        if n <= 0:
            print("Bad row count. break used.")
            break
        r = 1
        while r <= n:
            c = 1
            while c <= r:
                print("*", end="")
                c += 1
            print()
            r += 1
    elif opt == "2":
        st = int(input("Range start: "))
        en = int(input("Range end: "))
        if st > en:
            print("Invalid range, skipping...")
            continue
        totalSum = 0
        for val in range(st, en+1):
            if val % 2 == 0:
                print(val, "Even")
            else:
                print(val, "Odd")
            totalSum += val
        print("Total sum:", totalSum)
    elif opt == "3":
        print("Exit now. Thanks!")
        break
    else:
        print("Wrong input.")
