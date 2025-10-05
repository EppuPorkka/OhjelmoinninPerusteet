print("Program starting.\n")
print("Check multiplicative persistence.")
answer = int(input("Insert an integer: "))
steps = 0
num2 = None

while len(str(answer)) > 1:
    for i in range(0,len(str(answer))):
        if num2 == None:
            num2 = int(str(answer)[i])
            print(f"{int(str(answer)[i])} ",end="")
        else:
            num2 = num2 * int(str(answer)[i])
            print(f"* {int(str(answer)[i])} ",end="")
        
    answer = num2
    num2 = None
    steps += 1
    print(f"= {answer}")
print("No more steps.")

print(f"\nThis program took {steps} step(s)")

print("\nProgram ending.")