print("Program starting.")
num1 = int(input("Insert a positive integer: "))
steps = 0

print(f"{num1} -> ",end="")
while True:
    steps += 1
    if num1 % 2 == 0:
        num1 = num1 / 2
    else:
        num1 = num1 * 3 + 1
    
    if num1 == 1:
        print(int(num1))
        break
    else:
        print(f"{int(num1)} -> ",end="")

print(f"Sequence had {steps} total steps.")
print("\nProgram ending.")