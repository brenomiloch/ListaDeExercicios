saldo_conta = 200
valor_saque = float(input("Qual valor se quer retirar: "))

if valor_saque <= saldo_conta:
    # Se FOR true
    print("Saque Realizado no valor {}".format(valor_saque))
else:
    # Se FOR false
    print("O seu saldo é {}, seu valor de conta é {}.".format(valor_saque,saldo_conta))
