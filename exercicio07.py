Litros=float(input("E quantos litros você abasteceu?\n"))
Tipodecombustivel=input("Qual foi o combustivel que você solicitou?\n"
                        "G para Gasolina\n"
                        "E para Etanol\n")
vGas=5.80
vEta=4.90
if Tipodecombustivel=="G":
    ValorG = Litros*vGas
    print(f"Você abasteceu {Litros} litros e gastou R${ValorG:.2f}"!)
elif Tipodecombustivel=="E":
    ValorE = Litros * vEta
    print(f"Você abasteceu {Litros} litros e gastou R${ValorE:.2f}!")
else:
    print(f"Tipo de combusstivel não cadastrado!")