#constante
taxa1 = 20

#entrada
km = float(input('digite a distância da viagem em km: '))

def cal_preco_km(km):
    if km < 50:
        print('Não realizamos viagens para distâncias inferior a 50 km.')
    elif km < 200:
        taxa2 = 0.75
    elif km < 500:
        taxa2 = 0.60
    else:
        taxa2 = 0.50
    acresc_taxa = km * taxa2
    return acresc_taxa

#Cálculos
passagem = taxa1 + cal_preco_km(km)
print('Sua viagem com custará R$ {}.' .format(passagem))
#print(cal_preco_km(km))
