# EXEMPLO TABELA DA VERDADE DO OPERADOR not (NÃO).
print(not True)
print(not False)
print("===============================================")
# EXEMPLO 2:
X = 5
print("X={}".format(X))
print("Condição: X > 10")
if not X > 10:
    print("A condição é verdadeira.")
else:
    print("A condição é falsa.")
print("No exemplo anterior o valor de X é 5, então X não seria maior que 10, daria Falso, mas o 'not' inverte isso e torna Verdadeiro. ")
print("===============================================")
# Ele é usado para inverter o valor de uma expressão booleana, ou seja, se a expressão é verdadeira, o "not" a tornará falsa,
# e se a expressão é falsa, o "not" a tornará verdadeira.