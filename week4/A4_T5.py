print("Program starting.\n")

startingPoint = int(input("Insert starting point: "))
stoppingPoint = int(input("Insert stopping point: "))
inspectionPoint = int(input("Insert inspection point: "))
print("")
rule1met = False
rule2met = False

if startingPoint < stoppingPoint:
    rule1met = True
else:
    print("Starting point value must be less than the stopping point value.")

if inspectionPoint >= startingPoint and inspectionPoint <= stoppingPoint:
    rule2met = True
else:
    print("Inspection value must be within the range of start and stop.")


if rule1met and rule2met:
    print("First loop - inspection with break:")
    for i in range(startingPoint, stoppingPoint):
        if i == inspectionPoint:
            break
        else:
            if i == startingPoint:
                print(i, end="")
            elif i == stoppingPoint-1:
                print(f" {i}",end="")
            else:
                print(f" {i}", end="")
    print("\nSecond loop - inspection with continue:")
    for i in range(startingPoint, stoppingPoint):
        if i == inspectionPoint:
            continue
        else:
            if i == startingPoint:
                print(i, end="")
            elif i == stoppingPoint-1:
                print(f" {i}")
            else:
                print(f" {i}", end="")

print("\nProgram ending.")