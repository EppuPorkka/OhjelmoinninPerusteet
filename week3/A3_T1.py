print("Program starting.")
print("Insert two integers.")
int1 = int(input("Insert first integer: "))
int2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")

if int1 > int2:
    print("First integer is greater.")
elif int1 < int2:
    print("Second integer is greater.")
else:
    print("Integers are the same")

print("\nAdding integers together")
print(f"{int1} + {int2} = {int1 + int2}")

print("\nChecking the parity of the sum...")

if (int1 + int2) % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending.")