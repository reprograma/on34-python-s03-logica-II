'''
Qual o maior número?
Faça um programa que peça dois números inteiros de 0 a 100 e imprima o maior.

A saída deve ser parecida com isso: O maior número é X sendo que X deve ser o maior número dado pelo usuário.

Bônus1: tente fazer como função.

Bônus2: peça para o usuário 3 números e diga o mais alto.
'''
n1 = int(input('digite um núemnro:'))
n2 = int(input('digite outro núemnro:'))
if n1 > n2:
    print('{} é maio que {}.' . format(n1, n2))
else:
    print('{} é maior {}.' .format(n2, n1))

# número podem ser iguais