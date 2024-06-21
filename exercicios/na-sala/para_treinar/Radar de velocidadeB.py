#veloc_veiculo = int(input("Qual a velocidade do veículo?"))
#veloc_max = int(input("Qual a velocidade máxima da via?"))

def avalia_multa(veloc_veiculo, veloc_max):
    if veloc_veiculo <= veloc_max:
        print("O veículo passou na velocidade permitida")
    else:
        if veloc_veiculo <= (veloc_max * 1.2):
            print("O valor da multa é de R$ 200")
        else:
            print("O valor da multa é de R$ 350")

avalia_multa(80, 40)

avalia_multa(120, 100)

avalia_multa(35, 40)