print("Program starting.\n")
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
choice = input("Your choice: ")

if choice == '1':
    cel = float(input("Insert the amount of Celsius: "))
    print(f"{round(cel, 1)} °C equals to {round((cel * 1.8) + 32, 1)} °F")
elif choice == '2':
    fa = float(input("Insert the amount of Fahrenheit: "))
    print(f"{round(fa, 1)} °F equals to {round((fa - 32) / 1.8, 1)} °C")
elif choice == '0':
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")