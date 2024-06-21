def calcular_custo_viagem(distancia_km):
    if distancia_km < 0:
        print("Valor inválido! Por favor, digite uma distância positiva.")
        return None
    elif distancia_km < 50:
        print("A distância mínima para a viagem é de 50 km. Digite uma quilometragem válida.")
        return None
    
    if distancia_km <= 200:
        preco_por_km = 0.75
    elif distancia_km <= 500:
        preco_por_km = 0.60
    else:
        preco_por_km = 0.50
    
    valor_fixo = 20.00
    custo_total = (distancia_km * preco_por_km) + valor_fixo
    print(f"O custo da sua viagem de {distancia_km} km será de R$ {custo_total:.2f}")
    return custo_total


try:
    distancia_informada = float(input("Informe a distância da viagem em quilômetros: "))
    calcular_custo_viagem(distancia_informada)
except ValueError:
    print("Entrada inválida! Por favor, digite um número válido para a distância.")







