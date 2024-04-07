import os
os.system("cls||clear")


print("=====INICIO====")
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
nota1 = float(input("Digite sua 1 nota: "))
nota2 = float(input("Digite sua 2 nota: "))
nota3 = float(input("Digite sua 3 nota: "))
nota4 = float(input("Digite sua 4 nota: "))

media = (nota1+nota2+nota3+nota4) / 4

os.system("cls||clear")

print("=====RESULTADOS====")
print(f"Nome: ",nome)
print(f"Idade: ",idade)
print(f"Nota 1: ",nota1)
print(f"Nota 2: ",nota2)
print(f"Nota 3: ",nota3)
print(f"Nota 4: ",nota4)
print(f"Media: ", media)

