'''Custo da viagem

Uma empresa de viagens de ônibus contratou você para fazer um programa que calcule o preço das viagens. 
Cada viagem custa R$ 20,00 e mais um valor referente aos quilômetros viajados, conforme a tabela abaixo:

kms viajados	valor por km
Até 200km	R$ 0,75
Até 500km	R$ 0,60
mais de 500km	R$ 0,50
Calcule o valor e imprima a resposta como: Sua viagem com XX km custará R$ YY onde XX é o número de quilômetros e Y é o valor total a ser pago.

Seu programa não pode deixar o usuário:

calcular viagens com menos de 50km;
entrar com números negativos;
entrar com letras ou caracteres especiais que podem quebrar o programa.'''



'''
print("Calculando o preço da sua viagem:")
valor_viagem = 20
valor_por_km_rodado1 = 0.75
valor_por_km_rodado2 = 0.60
valor_por_km_rodado3 = 0.50

try: 
    viagem_realizada = float(input("Quantos km você irá viajar? "))
    if viagem_realizada > 500 : 
         print("Sua viagem com ", viagem_realizada, "Km custará R$:",valor_viagem + viagem_realizada*valor_por_km_rodado1)
    elif 200 < viagem_realizada <= 500 :
        print("Sua viagem com ", viagem_realizada, "Km custará R$:",valor_viagem + viagem_realizada*valor_por_km_rodado2)
    elif 50 <= viagem_realizada <= 200 :
        print("Sua viagem com ", viagem_realizada, "Km custará R$:",valor_viagem + viagem_realizada*valor_por_km_rodado3)
    elif 0 <= viagem_realizada < 50 :
        print("Não fazemos viagens com menos de 50 km")
    else:
         print("Você não pode digitar números negativos.Insira novamente um número válido!")
except ValueError:
    print("Entrada inválida. Por favor, digite um número válido.")'''

#Ou com função

print("Calculando o preço da sua viagem:")
try:
    def calc_viagem(km):
        if km <= 200:
            valor_por_km = 0.75
        elif km <= 500:
            valor_por_km = 0.60
        else:
            valor_por_km = 0.50
        custo_total = 20 + km * valor_por_km
        print("Sua viagem com ", km ," km custará R$ ", custo_total)

    km = float(input("Digite a distância em km da viagem: "))

    if km >= 50:
        calc_viagem(km)
    elif 0 <= km < 50 :
        print("Não fazemos viagens com menos de 50 km")
    else :
         print("Você não pode digitar números negativos.Insira novamente um número válido!")
except:
    print("Entrada inválida. Por favor, digite um número válido")










