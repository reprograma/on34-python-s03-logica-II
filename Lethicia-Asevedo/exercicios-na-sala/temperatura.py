##Como está a temperatura aí?
#Faça um programa que peça a temperatura atual em graus Celsius e imprima como 
# está o dia, conforme a tabela abaixo:

#Temperatura	Classificação
#Acima de 27 graus	dia quente
#De 20 a 27 graus	dia agradável
#Abaixo de 20 graus	dia frio
#Bônus Você pode começar perguntando se a entrada será em Celsius ou Fahrenheit e, 
# se for em Fahrenheit, transformar em Celsius. O cálculo é (°F - 32) / 1.8 = °C.

print("Olá, escolha a opção desejada: ")
escolha = int(input(print("""\nDigite 1 para começar com Fahreheint\nDigite 2 para começar com Celsius:""")))

graus_celsius = (graus_fahrenheit - 32) /1.8
graus_fahrenheit = (graus_celsius * 9/5) + 32

if escolha == 1: 
    print(f"A temperatura em graus Fahrenheit convertida para graus Celsius é: {graus_celsius}")
else:
    print(f"A temperatura em grus Celsius convertida para graus Fahrenheit é: {graus_fahrenheit} ")



