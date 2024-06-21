try:
    #constante
    taxa = 20
    #entrada
    km = float(input('Digite a distância da viagem em km (mínimo 50 km): '))
    if km < 0:
        print("Erro: A distância não pode ser negativa.")
    elif km < 50:
        print("Erro: A distância deve ser de pelo menos 50 km.")
    elif km < 200:
        preco_km = 0.75
    elif km <= 500:
        preco_km = 0.60
    else:
        preco_km = 0.50
    passagem = taxa + (km * preco_km)
    print('Sua viagem com {} km custará R$ {} .' .format(km, passagem))
except:
    print('O valor não pode ser inferior a 50')
    
    
