print("BEM VIDO NO JOGO DE ADIVINHAÇÃO!!")
chute = int(input("Digite seu chute: "))
numero_certo = 27
if chute == numero_certo:
    print("Acertou!!!!")
elif chute > numero_certo: 
    print("Você errou! O seu chute foi maior que o número secreto.")
else:
    print("Você errou! O seu chute foi menor que o número secreto.")