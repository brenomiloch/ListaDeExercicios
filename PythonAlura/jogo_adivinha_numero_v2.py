num_secreto = int(input("Digite um Num: "))
chute = int(input("Digite um chute: "))


acertou = chute == num_secreto
maior = chute > num_secreto
menor = chute < num_secreto

if acertou:
    print("Acertou")
else:
    if (maior):
        print("Número Maior")
    elif (menor):
        print("Número menor")
print("Fim do Jogo")