# Crie um programa em Python que receba a idade de uma pessoa em anos e imprima na tela a idade em meses e em dias.
# Considere que um ano tem 365 dias e um mês tem 30 dias. 
# Utilize os operadores aritméticos de divisão (/) e módulo (%) para calcular as idades em meses e em dias.
idade = int(input("Digite sua idade: "))
idademeses = idade * 12
idadedia = idade * 365
print("Idade em meses:",idademeses, "Idade em dias:",idadedia)