# Exercicio

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


