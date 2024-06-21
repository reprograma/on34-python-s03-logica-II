'''Faça um programa que peça dois números inteiros de 0 a 100 e imprima o maior.
A saída deve ser parecida com isso: O maior número é X sendo que X deve ser o maior número dado pelo usuário.
Bônus1: tente fazer como função.
Bônus2: peça para o usuário 3 números e diga o mais alto.'''

numero_1 = input("Insira o primeiro número (de 0 a 100)")
numero_2 = input("Insira o segundo número (de 0 a 100)")
numero_3 = input("Insira o terceiro número (de 0 a 100)")

resultado = int(max(numero_1, numero_2, numero_3))
print(resultado)