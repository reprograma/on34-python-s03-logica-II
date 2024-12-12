def viajar (distancia):
 valor_inicial =20.00

 if distancia <=0:
    preco_viagem = 0
    print("Não é permitido valores negativos")
 elif distancia <50:
      preco_viagem = 0
      print("Distância inválida, o trecho só será calculado a partir de 50km ")
 elif distancia <=200:
    preco_viagem = valor_inicial + (0.75 *distancia)
 elif distancia <= 500:
    preco_viagem = valor_inicial + (0.60 *distancia)
 elif distancia > 500:
    preco_viagem = valor_inicial + (0.50 *distancia)
 return preco_viagem   


try:
  distancia = float(input("Informe a distância da sua viagem: "))
  print("O valor da sua viagem é: R$ {:.2f}".format(viajar(distancia)))
except:
    print("inválido, digite uma opção válida")