def main():
    count = 0
    print("Program starting.")
    while True:
        showOptions()
        answer = askChoice()
        
        if answer == 1:
            print(f"Current count - {count}")
        elif answer == 2:
            count += 1
            print("Count increased!")
        elif answer == 3:
            count = 0
            print("Cleared count!")
        elif answer == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")

def showOptions():
    print("\nOptions:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")

def askChoice():
    choice = input("Your choice: ")
    if choice.isnumeric() == False:
        return None
    else:
        return int(choice)

main()

print("\nProgram ending.")