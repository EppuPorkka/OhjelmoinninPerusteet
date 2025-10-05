Cities = {
    'Finland':["Tampere", "Helsinki", "Lahti"],
    'Estonia':["Tallinn", "Tartu", "Pärnu"],
}

print(Cities['Finland'])
print(Cities['Finland'][0])

numbers = [1,2,3,4]
colors = ["red", "blue", "yellow", "green"]
colors.append("purple")
colors.sort()

print(colors, numbers)

for color in colors:
    print(f"my favovrite color is {color}")


Students = [
    {"name": "Eppu", "age": 24},
    {"name": "Aapo", "age": 24}
]

print(Students[0]["name"])

student = {"name": "Aapo", "age": 24}
for key in student:
    print(key)
    print(student[key])