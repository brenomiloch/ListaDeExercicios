# Faça um Programa que peça dois números e imprima o maior deles.

num_1 = int(input("Digite: "))
num_2 = int(input("Digite: "))

if num_1 >= num_2:
    maior = num_1
else:
    maior = num_2

print ("O maior número é {}".format(maior))
