# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas = float(input("Digite quanto vc recebe por hora: "))
horas_trabalhadas = float(input("Digite o números de horas trabalhadas no mês: "))
salario = horas * horas_trabalhadas

print("Seu salário do mês foi de: ",salario)