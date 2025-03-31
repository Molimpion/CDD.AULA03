# Mostrar nome, idade e salario
nome = input("Qual é o seu nome?\n")
idade = int(input("Quantos anos você tem?\n"))
salario = float(input("quanto você recebe por mês?\n"))
print(f"Prazer em conhecer você {nome}",
      f" então você tem {idade}",
      f" e já recebe {salario:.2f} por mês?")