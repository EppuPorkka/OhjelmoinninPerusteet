# simppeli ohjelma jolla testataan onko numero pariton vai parillinen
num = int(input("insert number: "))

if num % 2 == 0:
    print("parillinen")
else:
    print("pariton")


# simppeli ohjelma joka kertoo kumpi nimi on pidempi
name1 = input("eka nimi: ")
name2 = input("toka nimi: ")

if len(name1) > len(name2):
    print("eka nimi pidempi")
elif len(name1) < len(name2):
    print("toka nimi pidempi")
else:
    print("saman pituisia")