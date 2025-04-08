usuario = input("Digite o nome de usuário: ")

if usuario == "":
    print("O nome do usuário é obrigatório.")
else:
    senha = input("Digite a senha: ")
    if senha == "":
        print("A senha do usuário é obrigatória.")
    else:
        if (usuario == "admin" or usuario == "gestor") and senha == "1234":
            print("Acesso permitido.")
        else:
            print("Acesso negado.")
            if usuario != "admin" and usuario != "gestor" and senha != "1234":
                print("O nome do usuário e a senha estão incorretos.")
            elif usuario != "admin" and usuario != "gestor":
                print("O nome do usuário está incorreto.")
            elif senha != "1234":
                print("A senha está incorreta.")
