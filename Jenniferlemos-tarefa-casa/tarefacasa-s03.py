def calcular_custo_viagem(kms):
  custo_base = 20.00

  if kms <= 200:
    custo_por_km = 0.75
  elif kms <= 500:
    custo_por_km = 0.60
  else:
    custo_por_km = 0.50

  custo_total = custo_base + (kms * custo_por_km)
  return custo_total

try:
  kms = int(input("Digite a distância da viagem (em km): "))

  if kms < 50:
    print("A distância mínima da viagem é 50km. Por favor, tente novamente.")
  elif kms < 0:
    print("A distância não pode ser negativa. Por favor, tente novamente.")
  else:
    custo = calcular_custo_viagem(kms)
    print(f"Sua viagem com {kms} km custará R$ {custo:.2f}")

except:
  print("Por favor, digite um número válido de quilômetros.")
