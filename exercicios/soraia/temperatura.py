'''Faça um programa que peça a temperatura atual em graus Celsius e imprima como está o dia,
conforme a tabela abaixo:

Temperatura	Classificação
Acima de 27 graus	dia quente
De 20 a 27 graus	dia agradável
Abaixo de 20 graus	dia frio
Bônus: você pode começar perguntando se a entrada será em Celsius ou Fahrenheit e, 
se for em Fahrenheit, transformar em Celsius. O cálculo é (°F - 32) / 1,8 = °C.'''

temperatura = int(input("Qual a temperatura atual em graus Celsius?" ))

if temperatura >27:
  print("Seu dia está quente!")
elif temperatura >=20:
  print("Seu dia está agradável!")
else:
  print("Seu dia frio!")
  
  