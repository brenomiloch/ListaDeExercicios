# Crie um programa em Python que receba um número inteiro e verifique se ele é par ou ímpar. Para isso, utilize o
# operador de resto da divisão (%) para calcular o resto da divisão por 2.
num_01 = int(input("Digite um número: "))

if num_01 % 2 == 0:
    print("O número",num_01 ,  "é par")
else:
    print("O número",num_01 ,  "é impar")