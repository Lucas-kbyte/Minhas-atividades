ano = int(input("mano vamo que vamno"))

if(ano % 4 == 0 and  ano % 100 == 0) or ano % 400 == 0:

        print("É um ano bisexto")

else:
        print("Ano normal")