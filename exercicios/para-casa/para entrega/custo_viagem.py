# __________ CUSTO VIAGEM __________

print("Ola Bem Vindo(a) a companhia REPROGRAMA de viagens terrestres""\n")

print("Nossa companhia trabalha com quilometragem,confira:")
print("até 200km")
print("até 500km")
print("mais de 500km")

X = (input("Qual sera a distância do seu destino? "))

distancia = int(X)

valor_fixo = 20.00

if distancia < 50:
    print("Opção nao válida, a distancia minima para calcular é de 50km.")

elif 50 < distancia <= 200:
    custo_distancia = 0.75
elif 200 < distancia <= 500:
    custo_distancia = 0.60
elif distancia > 500:
    custo_distancia = 0.50

total = valor_fixo + (distancia * custo_distancia)
print(f"Sua viagem com {distancia} km custará R$ {total:.2f}")


    







