
nome = input("Digite o nome do aluno: ")
if nome == "":
    print("Algum dado obrigatório não foi preenchido ou houve o preenchimento incorreto de algum dado.")
else:
    nota1 = input("Digite a 1ª nota: ")
    nota2 = input("Digite a 2ª nota: ")
    nota3 = input("Digite a 3ª nota: ")
    nota4 = input("Digite a 4ª nota: ")
    if nota1 == "" or nota2 == "" or nota3 == "" or nota4 == "":
        print("Algum dado obrigatório não foi preenchido ou houve o preenchimento incorreto de algum dado.")
    else:
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)
        nota4 = float(nota4)
        if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10 or nota4 < 0 or nota4 > 10:
            print("Algum dado obrigatório não foi preenchido ou houve o preenchimento incorreto de algum dado.")
        else:
            media = (nota1 + nota2 + nota3 + nota4) / 4
            aulas = input("Digite a quantidade de aulas dadas: ")
            faltas = input("Digite a quantidade de faltas do aluno: ")
            if aulas == "" or faltas == "":
                print("Algum dado obrigatório não foi preenchido ou houve o preenchimento incorreto de algum dado.")
            else:
                aulas = int(aulas)
                faltas = int(faltas)
                if aulas <= 0 or faltas < 0 or faltas > aulas:
                    print("Algum dado obrigatório não foi preenchido ou houve o preenchimento incorreto de algum dado.")
                else:
                    presencas = aulas - faltas
                    frequencia = (presencas / aulas) * 100
                    print("Aluno:", nome)
                    if frequencia < 75:
                        print("Reprovado por falta.")
                        print("Não pode fazer recuperação devido a quantidade de faltas.")
                    else:
                        if media >= 7:
                            print("Aprovado.")
                        elif media >= 4 and media < 7:
                            print("Em recuperação.")
                            print("Pode fazer recuperação.")
                        else:
                            print("Reprovado por média.")
                            print("Não pode fazer a recuperação devido a média ser inferior a 4.")
