veloc_veiculo = int(input("Qual a velocidade do veículo?"))
veloc_max = int(input("Qual a velocidade máxima da via?"))

def checa_multa(veic, max)
if veic <= veloc_max:
    print("O veículo passou na velocidade permitida")
else:
    if veloc_veiculo <= (veloc_max * 1.2):
        print("O valor da multa é de R$ 200")
    else:
        print("O valor da multa é de R$ 350")
