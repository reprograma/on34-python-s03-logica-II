'''Faça um programa que peça dois números inteiros de 0 a 100 e imprima o maior.

A saída deve ser parecida com isso: O maior número é X sendo que X deve ser o maior número dado pelo usuário.

Bônus1: tente fazer como função.

Bônus2: peça para o usuário 3 números e diga o mais alto.'''

numero1 = int(input("Me diga um número inteiro entre 1 e 100 "))
numero2 = int(input("Me diga mais número inteiro entre 1 e 100 "))

if numero1 > numero2:
 print(numero1, "é maior que ", numero2)
if numero1 < numero2:
 print(numero1, "é menor que ", numero2)
 