print("Hello")

print("he said: \"Hello\" and kept walking") #käytä kenoviivaa jos ""  toisen "" sisällä
print("he said: Hello \n \r \t \b and \\ kept walking") #muita kenoviiva "komentoja"

exampleString = "text and numbers"
exampleInt = 100
exampleFloat = 1.5
exampleBoolean = True

#Name = input("Kirjoita nimesi:")
#Age = input("Kirjoita ikäsi:")
#print("Hei,", Name, Age + "v")

lause = "ABCDEFGHIJKLMN"
print(lause)
print(lause[0]) #antaa lauseen ekan merkin
print(lause[-2]) #antaa lauseen toiseksi viimeisen kirjaimen, vika olisi -1
print(lause[1:4]) #kirjoittaa kirjaimet kahden arvon väliltä. tässä BCD, D on 3. B on 1 (mistä indexistä mihin)
print(lause[:4]) # kirjoittaa 4 ekaa kirjainta
print(lause[-4:-1]) # printaa index -4 -> -1
print(lause[2:9:3]) # kirjoittaa joka kolmannen (3) kirjaimen alkaen index2 ja pysähtyy index 9
print(lause[::3])  #kirjoittaa joka kolmannen kirjaimen
print(lause[::-1]) #kirjoittaa stringin väärinpäin

nimi = "Eppu"
ika = 20
print(nimi + " " + str(ika))

num1 = int(input("anna luku1:"))
num2 = input("anna luku2:")
num3 = num1 + int(num2)
print(num3)

print((1+3)*5)


