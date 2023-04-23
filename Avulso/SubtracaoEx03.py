# Escreva um programa que converta uma temperatura de Fahrenheit para Celsius, utilizando:
# Fórmula: celsius = (fahrenheit - 32) * 5/9. 
# O programa deve solicitar ao usuário a temperatura em Fahrenheit e exibir o resultado em Celsius.

temp_fahrenheit = float(input("Digite a temperatura para conversão: "))
temp_celsius = (temp_fahrenheit - 32) * 5/9
print("A temperatura C° ",temp_celsius)