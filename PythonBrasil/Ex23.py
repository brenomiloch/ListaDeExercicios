# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# B. A mensagem "Reprovado", se a média for menor do que sete;
# C. A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))
media = (nota_1 + nota_2)/2
if media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reporvado")
elif media == 10:
    print("Aporvado")