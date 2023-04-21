# PythonBrasil

[**EstruturaSequencial**](https://wiki.python.org.br/EstruturaSequencial?action=fullsearch&context=180&value=linkto%3A%22EstruturaSequencial%22)


1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.

2. Faça um Programa que peça um número e então mostre a mensagem *O número informado foi [número]*.

3. Faça um Programa que peça dois números e imprima a soma.

4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

5. Faça um Programa que converta metros para centímetros.

6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
 total do seu salário no referido mês.

9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
 - C = 5 \* ((F-32) / 9).

10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    - A. o produto do dobro do primeiro com metade do segundo .
    - B. a soma do triplo do primeiro com o terceiro.
    - C. o terceiro elevado ao cubo.

12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a
 seguinte fórmula: (72.7\*altura) - 58

13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as
 seguintes fórmulas:
 - A. Para homens: (72.7\*h) - 58
 - B. Para mulheres: (62.1\*h) - 44.7

14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
 trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
 São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
 que leia a variável *peso* (peso de peixes) e calcule o excesso. Gravar na variável *excesso* a quantidade de quilos além do
 limite e na variável *multa* o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
 adequadas.

15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:
 - A. salário bruto.
 - B. quanto pagou ao INSS.
 - C. quanto pagou ao sindicato. d. o salário líquido.
 - E. calcule os descontos e o salário líquido, conforme a tabela abaixo:
   - + Salário Bruto : R$ IR (11%) : R$
   - - INSS (8%) : R$
   - - Sindicato ( 5%) : R$
   - = Salário Liquido : R$
   - ***Obs.: Salário Bruto - Descontos = Salário Líquido.***

16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
 pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
 pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

 - . Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

    - A. Comprar apenas latas de 18 litros;
    - B. Comprar apenas galões de 3,6 litros;
    - C. Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
    - E. arredonde os valores para cima, isto é, considere latas cheias.

18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em
 Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# ANOTAÇÕES

## QUESTÃO 03
**PROBLEMA:** Quando somamos 10+10, o resultado esperado é 20. No entanto, no código apresentado, o resultado gerado é 1010. Isso ocorre porque as variáveis "Num1" e "Num2" são tratadas como strings em vez de números inteiros(int) ou de ponto flutuante (float). Em vez de realizar a operação esperada de soma ele está concatenando as strings.
**SOLUÇÃO:** 
Para resolver o problema, é necessário converter as strings em números usando as funções int() ou float(). Essas funções permitem que as strings sejam convertidas em números inteiros ou de ponto flutuante (float), respectivamente. Com a conversão, o programa pode realizar a operação de soma aritmética esperada.



### EXEMPLOS: ###
A área de anotações das questões serve como um espaço de registro para anotar ideias, soluções de problemas e exemplos de códigos relacionados a questão da Python Brasil. É um local para registrar aprendizados e truques úteis, que podem ser referenciados futuramente para ajudar a resolver problemas similares ou para aumentar a eficiência na codificação. 
#### ❌ SEM int() ❌ #### 
~~~PYTHON
Num1 = ("Digite o primeiro número: ")
Num2 = ("Digite o secundo número ")
Resultado = Num1 + Num2
print("Sua soma foi de: " + Resultado)
~~~

~~~PYTHON
#Entrada de dados
Num1 = 10
Num2 = 10
Resultado = 1010
 ~~~

#### ✅ COM int() ✅ #### 
~~~PYTHON
Num1 = int(("Digite o primeiro número: "))
Num2 = int(("Digite o secundo número: "))
Resultado = Num1 + Num2
print("Sua soma foi de: " + Resultado)
~~~

~~~PYTHON
#Entrada de dados
Num1 = 10
Num2 = 10
Resultado = 20
 ~~~