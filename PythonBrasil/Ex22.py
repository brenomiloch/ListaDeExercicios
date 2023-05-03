# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Difite uma letra: ")
if letra in 'aeiouAEIOU':
    print("A letra {} é uma consoante.".format(letra))
else:
    print("A letra {} não é uma consoante.".format(letra))