words = []
characters = 0
print("Program starting.\n")
done = False

while done == False:
    word = input("Insert word (empty stops): ")
    if word == "":
        done = True
    else:
        words.append(word)

for i in range(0,len(words)):
    characters += len(words[i])

print("\nYou inserted:")
print(f"- {len(words)} words")
print(f"- {characters} characters")
print("\nProgram ending.")