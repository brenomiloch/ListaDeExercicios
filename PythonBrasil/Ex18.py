# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o 
# tempo aproximado de download do arquivo usando este link (em minutos).

TamanhoMb = float(input("Digite o tamanho de um arquivo em MB: "))
VelocidadeDownload = float(input("Digite a velocidade do link em Mbps: "))

Tempo = TamanhoMb/VelocidadeDownload/60

print("O tempo é:",Tempo)