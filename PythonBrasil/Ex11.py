# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # A. o produto do dobro do primeiro com metade do segundo .
    # B. a soma do triplo do primeiro com o terceiro.
    # C. o terceiro elevado ao cubo.

num_01 = int(input("Digita um número inteiro: "))
num_02 = int(input("Digita um número inteiro: "))
num_03 = float(input("Digita um número real: "))

ResultadoA = num_01 * 2 + (num_02/2)
ResultadoB = num_01 * 3 + num_03
ResultadoC = num_03 ** 3

print("A - ",ResultadoA)
print("B - ",ResultadoB)
print("C - ",ResultadoC)