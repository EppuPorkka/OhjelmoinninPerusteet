def main():
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")
    return None

def askName():
    nameinput = input("Insert name: ")
    return nameinput

def greetUser(PName):
    print(f"Hello {PName}!")
    return None

main()