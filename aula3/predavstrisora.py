import random 

pc = random.choice(["pedra", "papel", "tesoura"])

pessoa = input("vamos joga pedra papel e tesoura escolha ai"). capitalize()

print(f"Robo escolheu {pc}")
print(f"O playes escolheu {pessoa}")

if pessoa == pc:

        print("Deu empate!!")
    
elif(pessoa == "pedra" and pc == "tesoura") or (pessoa == "papel" and pc == "pedra") or (pessoa == "tesoura" and pc == "papel"):
        
        print("Você ganhou!")

elif pessoa not in ["pedra", "papel", "tesoura"]:

     print("Jogada invalida tente de novo")

else:
       
       print("Você perdeu")