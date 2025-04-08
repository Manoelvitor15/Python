valor_total = float(input("Insira o valor total da compra: "))
fidelidade = input("Cliente é fidelizado?")
print("1 = SIM")
print("2 = NÃO")
quant_compra = int(input("Informe a quantidade de compras do cliente: "))
cupom = input("Cliente tem cupom?")
print("1 = SIM")
print("2 = NÃO")
sim = 1
nao = 2
if (valor_total == "") and (fidelidade == "") and (quant_compra == "") and (cupom == ""):
    if valor_total > 0:
        if fidelidade != sim:
            print("Cliente não fidelizado")
            if cupom != sim:
                print("Cliente não possui cupom")
            else:
                print("Possui cupom com 10% de desconto")   
        else:
            print("Fidelizado.")

    else:
        print("Valor incorreto!")

else:
    print("Houve o preenchimento incorreto de algum dado")