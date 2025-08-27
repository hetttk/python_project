print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        rows = int(input("Enter the number of rows for the pattern: "))
        if rows <= 0:
            print("Invalid row count! Using break to stop pattern.")
            break
        for i in range(1, rows+1):
            for j in range(i):
                print("*", end="")
            print()
    elif choice == "2":
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        if start > end:
            print("Invalid range. Start must be less than End.")
            continue
        total = 0
        for num in range(start, end+1):
            if num % 2 == 0:
                print("Number", num, "is Even")
            else:
                print("Number", num, "is Odd")
            total += num
        print("Sum of all numbers from", start, "to", end, "is:", total)
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option, try again.")
