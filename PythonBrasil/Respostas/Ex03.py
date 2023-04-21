# Faça um Programa que peça dois números e imprima a soma.

Num1 = int(input("Digite o primeiro numero: "))
Num2 = int(input("Digite o secundo numero: "))

Resultado = Num1 + Num2

print("Sua soma deu: " + Resultado)

#ANOTAÇÃO: A Soma de 10+10 não foi 20 e sim 1010, para corrigir foi necessario adicionar
# o int()
#PROBLEMA: Num1= input("Digite o primeiro numero: ") vai ser tratado como string por isso a necessidade de colocar int()
