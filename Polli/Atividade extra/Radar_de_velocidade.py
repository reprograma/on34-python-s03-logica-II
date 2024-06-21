#Identificação
placa = str(input('Qual a placa do carro (sete digitos com letras e números?'))
#Variáveis
kmporh = int(input('Qual a velocidade do carro?'))
maxi = int(input('Qual a velocidade maxima da via?'))

#constantes
multa = 200
multa2 = 350

#Calculo da multa

if kmporh <= maxi:
    print('O carro {} está dentro do limite de velocidade.' .format(placa))
elif kmporh > maxi + (maxi * 0.2):
    print('O carro {} foi multado em R$ {}, por exceder a velocidade em mais de 20 porcento do limite.' .format(placa, multa2))
else:
    print('O carro {} foi multado em R$ {}, por exceder a velocidade.' .format(placa, multa))
