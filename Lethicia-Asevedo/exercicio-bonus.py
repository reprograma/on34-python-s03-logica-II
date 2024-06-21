## Exercício custo da viagem com função

def calculo_viagem(km_viajado):

    if km_viajado < 0:
        print("Digite valores válidos por favor!")
    elif km_viajado < 50:
        print("Sua viagem não pode ter menos de 50km, digite uma quilometragem válida por favor")
    elif km_viajado <= 200:
        valor_viagem = (km_viajado * 0.75) + 20.00
        print(f"Sua viagem com {km_viajado}kms custará R$ {valor_viagem}")
    elif km_viajado <= 500:
        valor_viagem = (km_viajado * 0.60) + 20.00
        print(f"Sua viagem com {km_viajado}kms custará R$ {valor_viagem}")
    else:
        valor_viagem = (km_viajado * 0.50) + 20.00
        print(f"Sua viagem com {km_viajado}kms custará R$ {valor_viagem}")

    return valor_viagem

try:
    distancia = float(input("Digite quantos Kms tem sua viagem por favor: "))
    calculo_viagem(distancia)
except:
    print("Por favor, digite um valor válido.")