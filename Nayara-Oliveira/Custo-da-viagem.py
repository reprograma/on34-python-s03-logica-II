try:
    def calcular_viagem(distancia):
        if distancia <= 200:
            valor_por_km = 0.75
        elif distancia <= 500:
            valor_por_km = 0.60
        else:
            valor_por_km = 0.50
        custo_total = 20 + valor_por_km * distancia
        print(f"Sua viagem com {distancia} km custará R${custo_total}.")

    print("Bem vinda, vamos calcular o preço da sua viagem?")
    distancia = float(input("Por favor, informe os quilômetros a serem viajados: "))
    
    if distancia >= 50:
        calcular_viagem(distancia)
    else:
        print("Infelizmente, não há viagens com percurso menor que 50 km")
except:
    print("Erro: letras ou caracteres especiais não devem ser inseridos. Por favor, insira um valor numérico")