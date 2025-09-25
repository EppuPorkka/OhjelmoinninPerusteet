print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")
print("\nOptions:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        value = float(input("Insert meters: "))
        print(f"{round(value,1)} m is {round(value/1000,1)} km")
    elif choice == 2:
        value = float(input("Insert kilometers: "))
        print(f"{round(value,1)} km is {round(value*1000,1)} m")
    elif choice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice == 2:
    print("\nLength options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        value = float(input("Insert grams: "))
        print(f"{round(value,1)} g is {round(value*0.002205,1)} lb")
    elif choice == 2:
        value = float(input("Insert pounds: "))
        print(f"{round(value,1)} lb is {round(value*453.59237,1)} g")
    elif choice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")