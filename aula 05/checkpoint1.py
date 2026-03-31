import random
vidas = 7

num = random.randint(1, 100)

print("Ola jogador, eu escolhi um numero de 1 a 100, e você terá que adivinhar muehehehe >:3")
print("Ah, eu esqueci de fala que você tem 7 tentativas")


while True:
        
        num_esc = int(input("Digite seu número aqui\n"))
        vidas -= 1

        if vidas == 0:
                print(f"Você perdeu esse era o numero {num}")
                break

        elif num_esc == num:
                print("Você acertou!!!")
                print(f"Número de tentativas {vidas}")
                break
        
        elif num_esc < num:
                print("Você errou, aqui vai uma dica, o número é maior")
                print(f"Aqui quantas tentativas você tem {vidas}")
        
        else:
                print("Você errou, aqui vai uma dica, o número é menor")
                print(f"Aqui quantas tentativas você tem {vidas}")