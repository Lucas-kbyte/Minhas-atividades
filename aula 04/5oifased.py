
pala = input("Escreva uma palavra")

for letra in pala:

            print(f"-{letra}", end = " ")

for letra in pala[:: -1]:

            print(f"-{letra}", end = " ")