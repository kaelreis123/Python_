import os
os.system("cls||clear")

print(f"===Inicio==")
Nome = str(input(f"Digite seu nome: "))
ano = int(input(f"Digite o ano de nascimento: "))


idade = 2024 - ano
print(f"Idade: {idade}")
if idade > 18:#(and (e) &&)(or (ou) ||)# and idade > 65
    print("MAIOR DE IDADE")
else:
    print("MENOR DE IDADE")
