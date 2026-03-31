pesado = float(input("Qual é o teu peso??"))

gigante = float(input("Qual é atua altura"))

imc = (pesado/(gigante**2))

imc = round(imc,2)

print(f"Então cuzão, esse é o teu peso {imc}")

if imc >= 18.5:
     
        print("Caralho mano, tu ta abaixo do peso")

elif imc >= 18.5 and imc <= 24.9:
     
        print("Você esta com peso normal")

elif imc >= 25.0 and imc <= 29.9:
       
        print("Você é gordo, ta com excesso de peso")

elif imc >= 30.0:
      
        print("Obeso!!!")