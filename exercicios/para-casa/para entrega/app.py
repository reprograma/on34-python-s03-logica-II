def calcular_preco_viagem(km):
    # Define o custo fixo da viagem
    custo_fixo = 20.00
    
    # Calcula o custo por km baseado na distância
    if km <= 200:
        custo_por_km = 0.75
    elif km <= 500:
        custo_por_km = 0.60
    else:
        custo_por_km = 0.50
    
    # Calcula o custo total da viagem
    custo_total = custo_fixo + (custo_por_km * km)
    return custo_total

def main():
    while True:
        try:
            # Solicita ao usuário a quantidade de quilômetros
            km = float(input("Digite a quantidade de quilômetros para a viagem (mínimo 50km): "))
            
            # Verifica se o valor está dentro do intervalo permitido
            if km < 50:
                print("A quantidade de quilômetros deve ser pelo menos 50km.")
                continue
            if km < 0:
                print("A quantidade de quilômetros não pode ser negativa.")
                continue
            
            # Calcula o preço da viagem
            preco = calcular_preco_viagem(km)
            
            # Imprime o resultado
            print(f"Sua viagem com {km:.2f} km custará R$ {preco:.2f}")
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para os quilômetros.")

if __name__ == "__main__":
    main()
