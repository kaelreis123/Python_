#Elabore um algoritmo para ler um valor e escrever a mensagem:
#É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário
#escrever “NÃO É MAIOR QUE 10!

import os
os.system("Cls||clear")

numero = int(input("Digite um numero: "))
if numero > 10:
    print("Maior que 10")
else: print("Menor que 10")