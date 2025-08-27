print("Mini Personal Data Collector")
print("Answer a few questions below.")

# Input with basic type casting
person_name = input("What is your name? ")
years_old = int(input("How old are you? "))
heightM = float(input("Height in meters: "))
favNumber = int(input("Favourite number: "))

# Display information neatly
print("\n== Info ==")
print(f"person_name: {person_name} | type: {type(person_name)} | id: {id(person_name)}")
print(f"years_old: {years_old} | type: {type(years_old)} | id: {id(years_old)}")
print(f"heightM: {heightM} | type: {type(heightM)} | id: {id(heightM)}")
print(f"favNumber: {favNumber} | type: {type(favNumber)} | id: {id(favNumber)}")

# Simple maths
made_year = 2025 - years_old
print(f"\nYou were probably born in: {made_year}")
print("Thanks for trying this out!")