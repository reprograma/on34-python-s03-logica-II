try:
     km = float(input('Quantos quilometros terá sua viagem? ')) 
     
     if km <= 0:
          print('Não calculamos viagens com menos de 50km, valor negativo ou igual a zero')
     
     elif km <= 49:
          print('Não calculamos viagens com menos de 50km, valor negativo ou igual a zero')
     
     elif km >= 50 and km <= 200:
          valor = km * 0.75
          print('Sua viagem com ', km, 'km custará R$ ', valor)
     
     elif km >= 201 and km <= 500:
          valor = km * 0.60
          print('Sua viagem com ', km, 'km custará R$ ', valor)
     else:
          km >= 501
          valor = km * 0.50
          print('Sua viagem com ', km, 'km custará R$ ', valor)
except:
     print('Fim')