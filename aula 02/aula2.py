user_bd = "baitola"
senha_bd = "6969"

user = input("User: ")
pwd = input("Senha: ")

acesso = (user == user_bd) and (pwd == senha_bd)

print(f"Acesso liberado? {acesso}")