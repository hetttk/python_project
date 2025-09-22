print("Personal Data Sheet")
print("-------------------")

# Asking user data
studentName = input("Name: ")
AGE = int(input("Age: "))
ht_m = float(input("Height (m): "))
bestNo = int(input("Favourite number: "))

# Using string concatenation style
print("\nHere are your values:")
print("studentName: " + studentName + " | type: " + str(type(studentName)) + " | id: " + str(id(studentName)))
print("AGE:", AGE, "| type:", type(AGE), "| id:", id(AGE))
print("ht_m:", ht_m, "| type:", type(ht_m), "| id:", id(ht_m))
print("bestNo:", bestNo, "| type:", type(bestNo), "| id:", id(bestNo))

# Birth year math
guessYear = 2025 - AGE
print("\nBirth year (approx):", guessYear)
print("Thanks for filling the sheet!")