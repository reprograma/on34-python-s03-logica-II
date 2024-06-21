def valorviagem (quilometros):
  valor_inicial=20.00

  if quilometros <50:
    print(" a viagem não pode ser calculada")
  elif quilometros <=200:
    preco_total = valor_inicial + (0.75*quilometros)
  elif quilometros <=500:
    preco_total = valor_inicial + (0.60*quilometros)
  elif quilometros >500:
    preco_total = valor_inicial + (0.50*quilometros)

  return preco_total
try:
  quilometros = float(input("Digite os quilometros da viagem :"))
  print (" o preço total da viagem é R$:",valorviagem(quilometros))
except :
  print(" digite valores válidos")