'''Faça um programa que parte a temperatura atual em graus Celsius e imprima como está o dia, conforme tabela abaixo:

Temperatura	Classificação
Acima de 27 graus	dia quente
De 20 a 27 graus	dia agradável
Abaixo de 20 graus	dia frio
Bônus: você pode começar a perguntar se a entrada será em Celsius ou Fahrenheit e, se for em Fahrenheit, transformar em Celsius. O cálculo é (°F − 32) × 1,8 = °C.'''



temperatura_dia = float(input("Qual a temperatura? "))

if temperatura_dia >= 27:
    print("Dia está quente")
elif temperatura_dia >= 20:
    print("Dia está agradável")
else:
    print("Dia está frio")
