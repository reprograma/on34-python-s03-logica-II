print(" |||"  "Departamento de Trânsito"  "|||\n")

velocidade_veiculo = int(input("Por favor, digite a velocidade do veículo (em km/h): "))
velocidade_max_via = int(input("Digite a velocidade máxima da via (em Km/h): "))

def calculo_velocidade():

    global velocidade_veiculo
    global velocidade_max_via
    limite_percentual = 0.2
    limite_velocidade = velocidade_max_via * (1 + limite_percentual)

    if velocidade_veiculo <= velocidade_max_via:
        print("Dentro da velocidade permitida. Não há multa.")
    elif velocidade_veiculo <= limite_velocidade:
        print("Acima da velocidade permitida. Multa de R$ 200,00.")
    else:
        print("Velocidade muito alta. Multa de R$ 350,00.")


calculo_velocidade()        