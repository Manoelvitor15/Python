print("Acesso Restrito")

usuario = input("Digite o usuário: ")
senha = input("Digite sua senha: ")



if usuario != "":
    if senha != "":
        if (usuario != "admin") and (usuario != "gestor") and senha != "1234":
            print("O nome do usuário e a senha estão incorretos")
            if (usuario == "admin") and (usuario ==  "gestor"):
                print("Acesso permitido")
                
                if senha == "1234":
                    print("acesso permitido")

                else:
                    print("Senha informada está incorreta")
                    print("Acesso negado")
            else:
                print("Nome de usuário incorreto")
                print("Acesso negado")  
        else:
            print("Acesso permitido")
    else:
        print("A senha do usuário é obrigatória")
else:
    print("O nome do usuário é obrigatório")


