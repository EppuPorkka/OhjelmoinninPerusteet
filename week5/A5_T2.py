def main():
    print("Program starting.")
    word = input("Insert word: ")
    print("")
    frameWord(word)
    print("\nProgram ending.")
    return None

def frameWord(Pword):
    print("*************")
    print(f"* {Pword} *")
    print("*************")
    return None

main()