aluno = input("Digite o nome do aluno: ")
print("")
nota1 = float(input("Informe a nota do 1º Bimestre: "))
nota2 = float(input("Informe a nota do 2º Bimestre: "))
nota3 = float(input("Informe a nota do 3º Bimestre: "))
nota4 = float(input("Informe a nota do 4º Bimestre: "))
print("")
media  = (nota1+nota2+nota3+nota4) / 4

if (media >= 7) and (media <= 10):
    print(f"{aluno} está APROVADO com média {media}")
elif (media >= 4) and (media < 7):
    print(f"{aluno} está em RECUPERAÇÃO com média {media}")

else:
    print(f"{aluno} está em REPROVADO com média {media}")