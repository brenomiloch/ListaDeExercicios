# Escreva um programa em Python que receba um número inteiro do usuário e verifique se ele é divisível por 3 e por 5 
# ao mesmo tempo. Em seguida, imprima na tela a mensagem "divisível" ou "não divisível", conforme o caso.
num_01 = int(input("Digite um número: "))
if num_01 % 3 == 0 and num_01 % 5 == 0:
    print(num_01,"é divisível.")
else:
    print(num_01,"não é divisível.")