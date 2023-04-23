# Crie um programa em Python que receba o salário atual de um funcionário e o percentual de aumento que ele receberá. O programa deve calcular o novo salário do
# funcionário e imprimir na tela.

salario = float(input("Digite seu salario: "))
peraumento = float(input("Digite o percentual de aumento: "))

aumento = (peraumento/100)* salario

total = aumento + salario

print("Total salario; ",total)