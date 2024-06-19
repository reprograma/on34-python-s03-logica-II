print("\n------------------------------------------")
print("CÁLCULO DE VIAGEM")
print("------------------------------------------\n")
print("Vamos calcular sua viagem rodoviária em nossa empresa?")
print("------------------------------------------\n")

print("O cálculo é realizado a partir de taxa fixa- R$20,00- e valor de acordo com a quilometragem viajada (visualize tabela abaixo)")
print("------------------------------------------\n")


tabela = f"""
| kms viajados  | valor por km |
| ------------- | -----------  |
| Até 200km     | R$ 0,75      |
| Até 500km     | R$ 0,60      |
| Mais de 500km | R$ 0,50      |
"""
print(tabela)


def calviagem (quilometros):
  taxa =20.00

  if quilometros <50:
    print("Sua viagem não pode ser calculada. Não realizamos trechos com menos de 50km.")
  elif quilometros <=200:
    preco_total = taxa + (0.75*quilometros)
  elif quilometros <=500:
    preco_total = taxa + (0.60*quilometros)
  elif quilometros >500:
    preco_total = taxa + (0.50*quilometros)

  return preco_total
try:
  quilometros = float(input("Digite os quilometros da viagem :"))
  print ("Sua viagem com ", quilometros , "km custará o preço total de R$:", calviagem(quilometros))
except :
  print(" digite valores válidos")