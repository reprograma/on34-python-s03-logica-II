# Exercicio

#Uma empresa de viagens de ônibus contratou você para fazer um programa que calcule o preço das viagens. Cada viagem custa R$ 20,00 
#e mais um valor referente aos quilômetros viajados, conforme a tabela abaixo:
#kms viajados	valor por km
#Até 200km	R$ 0,75
#Até 500km	R$ 0,60
#mais de 500km	R$ 0,50
#Calcule o valor e imprima a resposta como: Sua viagem com XX km custará R$ YY onde XX é o número de quilômetros e Y é o valor total a ser pago.
#Seu programa não pode deixar o usuário:

#calcular viagens com menos de 50km;
#entrar com números negativos;
#entrar com letras ou caracteres especiais que podem quebrar o programa.
#Bônus: use função ;)

import math


def valor_variavel(km):
    y = 20.00
    x1 = (0.75 * km) + y
    x2 = (0.60 * km) + y
    x3 = (0.50 * km) + y
    if (km >=50 and km <=200):
     print(f'Sua viagem com',km,'km custará R$ {:,.02f}'.format(x1))
    elif (km >200 and km <=500):
     return print('Sua viagem com',km,'km custará R$ {:,.02f}'.format(x2))
    elif (km >500): 
     return print('Sua viagem com',km,'km custará R$ {:,.02f}'.format(x3))
    else:
       (km <50)
       return print('Você não digitou um número válido!🚨')

try:
   print('Vamos calcular o preço das viagens por km 🚌')
   km = int(input('Insira um número a partir de 50km: '))
   valor_variavel(km)
except:
    print('Você não digitou um número válido!🚨')
