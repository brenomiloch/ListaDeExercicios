# Escreva um programa em Python que receba um número inteiro do usuário e verifique se ele é par ou ímpar.
# Em seguida, imprima na tela a mensagem "par" ou "ímpar", conforme o caso.
num_01 = int(input("Digite num: "))
if num_01 % 2 == 0:
    print(num_01,"é par.")
else:
    print(num_01,"é impar.")