'''Custo da Viagem'''


try:
  km_viajado = float(input("Quantos quilômetros será sua viagem?"))
  custo_viagem_ate200 = (km_viajado * 0.75) + 20
  custo_viagem_ate500 = (km_viajado * 0.60) + 20
  custo_viagem_mais500 = (km_viajado * 0.50) + 20
  
except:
  print("Você só pode colocar km em números nesse programa!")

def custo_viagem():
  if km_viajado < 0:
    print("Você não pode digitar valores negativos! ")
  elif km_viajado < 50:
    print("Sua viagem com ", km_viajado, " km " "não pode ser calculado, nosso mínimo é 50km ")
  elif km_viajado <= 200:
    print("Sua viagem com ", km_viajado, "km" " custará ", custo_viagem_ate200, " reais ")
  elif km_viajado <= 500:
    print("Sua viagem com ", km_viajado, "km" " custará ", custo_viagem_ate500, " reais ")
  elif km_viajado > 500:
    print("Sua viagem com ", km_viajado, "km" " custará ", custo_viagem_mais500, " reais ")
    

custo_viagem()

