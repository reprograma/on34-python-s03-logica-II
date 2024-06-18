passagem = 20

def calc_viagem(km_viajado, taxa):
    return km_viajado * taxa + passagem

try:
    km_viajado = float(input('Quantos quilômetros você viajou?\n'))

    if km_viajado < 0:
        print('Somentente números positivos.')

    elif km_viajado < 50:
        print('Quilometragem mínima de 50 km.')

    else:
        if km_viajado <= 200:
            custo_total = calc_viagem(km_viajado, 0.75)

        elif km_viajado <= 500:
            custo_total = calc_viagem(km_viajado, 0.60)

        else:
            custo_total = calc_viagem(km_viajado, 0.50)

        print(f'Sua viagem com {km_viajado} km custará R$ {custo_total}!')

except:
    print('Somente números.')
