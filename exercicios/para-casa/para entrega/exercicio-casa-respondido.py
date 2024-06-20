'''Uma empresa de viagens de ônibus contratou você para fazer um programa que calcule o preço das viagens. 
Cada viagem custa R$ 20,00 e mais um valor referente aos quilômetros viajados, conforme a tabela abaixo:

kms viajados	    valor por km
Até 200km	        R$ 0,75
Até 500km	        R$ 0,60
mais de 500km	    R$ 0,50

Calcule o valor e imprima a resposta como: Sua viagem com XX km custará R$ YY onde XX é o número de quilômetros e 
Y é o valor total a ser pago.

Seu programa não pode deixar o usuário:

calcular viagens com menos de 50km;
entrar com números negativos;
entrar com letras ou caracteres especiais que podem quebrar o programa.'''

distancia = float(input("Qual a distância gostaria de viajar? "))

conta1 = float(20+(distancia*0.75))
conta2 = float(20+(distancia*0.60))
conta3 = float(20+(distancia*0.50))

if distancia <= 200:
    print("O valor da sua viagem é: R$ ", conta1)
elif distancia <= 500:
    print("O valor da sua viagem é: R$ ", conta2)
else:
    print("O valor da sua viagem é: R$ ", conta3)
