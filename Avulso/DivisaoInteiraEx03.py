# Escreva um programa que calcule o quociente e o resto da divisão inteira entre dois números inteiros.
# Receba os números do usuário e imprima na tela o resultado do quociente e do resto.
num_01 = int(input("Digite um número: "))
num_02 = int(input("Digite um número: "))
quociente = num_01 // num_02
resto = num_01 % num_02
print("O quociente:", quociente)
print("O resto:", resto)