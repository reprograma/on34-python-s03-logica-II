print("Olá, seja-bem vindo! Calcule o valor de sua viagem.")

def calcular_preco_viagem(kms):
    if kms <= 200:
        preco_por_km = 0.75
    elif kms <= 500:
        preco_por_km = 0.60
    else:
        preco_por_km = 0.50
    
    preco_total = 20 + (kms * preco_por_km)
    return preco_total

def main():
    while True:
        try:
            kms = int(input("Digite a distância da viagem em quilômetros: "))
            if kms < 50:
                print("A viagem deve ser de pelo menos 50 km. Tente novamente.")
                continue
            if kms < 0:
                print("A distância não pode ser negativa. Tente novamente.")
                continue
            
            preco = calcular_preco_viagem(kms)
            print(f"Sua viagem com {kms} km custará R$ {preco:.2f}")
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()