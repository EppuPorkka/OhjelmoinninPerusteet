print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")
print("\nOptions:\n1 - Print welcome message\n0 - Exit")
choice = int(input("Your choise: "))

if choice == 1:
    print(f"Welcome {name}!")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")