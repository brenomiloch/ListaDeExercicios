num_secreto = 30
tentativas = 3
rodada = 1
while rodada <= tentativas:
    print("Tentativa {} de {} ".format(rodada,tentativas))
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
    rodada = rodada + 1
print("Fim do Jogo")    