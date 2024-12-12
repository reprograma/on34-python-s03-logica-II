#Identificação
Nome = input('Digite o nome do paciente:')

#Variáveis
Peso = float(input('Digite o peso (kg) do paciente:'))
h = float(input('Digite altura (m) do paciente:'))

#Calculo
IMC = Peso / (h ** 2)

#condições
if IMC < 18.5:
    print('Oi, {}! Sua classificação é de Magresa.' .format(Nome))
elif IMC <= 24.9:
    print('Oi, {}! Sua classificação é normal.'.format(Nome))
elif IMC <= 29.9:
    print('Oi, {}! Sua classificação é de sobrepeso.'.format(Nome))
elif IMC <= 39.9:
    print('Oi, {}! Sua classificação é de obesidade.'.format(Nome))
else:
    print('Oi, {}! Sua classificação é de obesidade grave')
