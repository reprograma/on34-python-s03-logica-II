print("Custo da viagem")

def custo_viagem (x,y,z):
    return x + (y*z)


custo_fixo = 20

try:
    km_viagem_desejada = int(input("Digite aqui a quilometragem da viagem desejada, a partir de 50km:"))

    if km_viagem_desejada < 50:
        print("Você deve escolher uma kilometragem a partir de 50 para calcular o custo da sua viagem")

    elif km_viagem_desejada <= 200:
        custo_viagem_total = custo_viagem(custo_fixo, km_viagem_desejada, 0.75)

    elif km_viagem_desejada <= 500:
        custo_viagem_total =  custo_viagem( custo_fixo, km_viagem_desejada, 0.60)

    else: 
        custo_viagem_total = custo_viagem(custo_fixo, km_viagem_desejada, 0.50)

    print(" Sua viagem com", km_viagem_desejada , "KM custará R$" , custo_viagem_total)

except:
    print(" Você não pode entrar com numero negativo, letra ou caracter especial, por favor entre com KM apartir de 50")
