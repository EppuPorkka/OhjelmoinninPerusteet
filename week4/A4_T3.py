print("Program starting.\n")
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
print("\nStarting while loop:")

while start < stop+1:
    # if statementin avulla poistetaan viimeisen numeron perästä tyhjä välilyönti.
    if start == stop: 
        print(start)
    else:
        print(start,end=" ")
    start += 1

print("\nProgram ending.")