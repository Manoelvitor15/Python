valor = input("Digite o valor total da compra: ")
fidelizado = input("O cliente é fidelizado? (1 - Sim | 2 - Não): ")
compras = input("Quantidade de compras já realizadas: ")
cupom = input("O cliente tem cupom especial? (1 - Sim | 2 - Não): ")

if valor == "" or fidelizado == "" or compras == "" or cupom == "":
    print("Houve o preenchimento incorreto de algum dado.")
else:
    valor = float(valor)
    compras = int(compras)
    if valor <= 0 or compras < 0 or (fidelizado != "1" and fidelizado != "2") or (cupom != "1" and cupom != "2"):
        print("Houve o preenchimento incorreto de algum dado.")
    else:
        if (fidelizado == "1" and compras > 5) or cupom == "1":
            desconto = valor * 0.10
            total = valor - desconto
            print("Cliente tem direito ao desconto.")
        else:
            total = valor
            print("Cliente não tem direito ao desconto.")

        print("Valor total a pagar: R$ ", round(total, 2))
