def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")

def collectWords():
    allWords = ""
    while True:
        userInput = input("Insert word(empty stops): ")
        if not userInput == "":
            if allWords == "":
                allWords = userInput
            else:
                allWords = (allWords + "|" + userInput)
        else:
            break
    return allWords

def analyseWords(wordList):
    wordTable = wordList.split("|")
    numOfWords = len(wordTable)
    numOfCharacters = sum(len(v) for v in wordTable)
    print(f"- {numOfWords} Words")
    print(f"- {numOfCharacters} Characters")
    print("- {:.2f} Average word length".format(numOfCharacters / numOfWords))

main()