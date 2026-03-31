gorjeta = int(input("Quanto você irá dar de gorjeta?"))

print(f"Você deu {gorjeta} então recebera 10% de desconto")

gorjeta = gorjeta * 0.10

conta = int(input("E quanto deu a conta?"))

total = float (conta + gorjeta)

print(f"então o total é de {total}")
