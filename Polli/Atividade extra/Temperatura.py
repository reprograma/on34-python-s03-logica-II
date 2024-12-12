#Entradas
temp = float(input('Digite a temperatura atual: '))
unidade = input('Digite 1 para graus Celsius e 2 para graus Fahrenheit: ')

#condição 
if unidade == 1:
    celcius = temp
else:
    #Conversor de temperatura °F para °C
    def converte(temp):
        celcius = ((temp - 32) / 1.8)
        return celcius
celcius = converte(temp)

if celcius > 27:
    print('Como está o dia aí?\nDia quente')
elif celcius >= 20:
    print('Como está o dia aí?\nDia agradável')
else:
    print('Como está o dia aí?\n28Dia frio')


                   