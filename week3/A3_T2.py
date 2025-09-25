print("Program starting.")
print("String comparisons")
word = input("Insert first word: ")
character = input("Insert a character: ")
if character in word:
    print(f"Word \"{word}\" contains character \"{character}\"")
else:
    print(f"Word \"{word}\" doesn't contain character \"{character}\"")

word2 = input("Insert second word: ")

if word < word2:
    print(f"The first word \"{word}\" is before the second word \"{word2}\" alphabetically.")
elif word2 < word:
    print(f"The second word \"{word2}\" is before the first word \"{word}\" alphabetically.")
else:
    print(f"Both inserted words are the same alphabetically, \"{word}\"")
print("Program ending.")