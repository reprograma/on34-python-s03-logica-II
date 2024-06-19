def titulo(txt):
   print("=" * 30)
   print(txt)
   print("=" * 30)

titulo(" Calculo Custo da Viagem!")        

# Foi criada uma função e dentro dela trabalhamos com condicionais If, Else e Elif.  
def calcular_custo_viagem(km):
    valor_base = 20.00

# Dentro de cada condição calculamos km percorrido com valor de custo da viagem,
# E retornamos com o print o resultado!    
    if km < 50:
     print("A distância mínima para uma viagem é de 50km. Por favor, insira uma distância válida.")

    elif km <= 200:
      valor_km = 0.75
      valor_adicional = km * valor_km  
      valor_total = valor_base + valor_adicional   
      print(f"Sua viagem com {km} km custará R$ {valor_total:.2f}")
      
    elif km <= 500:
      valor_km = 0.60
      valor_adicional = km * valor_km  
      valor_total = valor_base + valor_adicional   
      print(f"Sua viagem com {km} km custará R$ {valor_total:.2f}")  
    else:
      valor_km = 0.5 
      valor_adicional = km * valor_km  
      valor_total = valor_base + valor_adicional   
      print(f"Sua viagem com {km} km custará R$ {valor_total:.2f}")



#Foi utilizado Try e Except nesse bloco para criar exceções durante a execução do código.
#Utilizamos estrutura condicionais para especificar o que não seria aceito no valor de entrada input. 
try:
    distancia = float(input("Insira quantos km por viagem: "))
    
    if distancia < 0:
        print("Por favor, insira um valor numérico que não seja negativo!")

    else:
        calcular_custo_viagem(distancia)
        
except:
    print("Por favor, não insira letras ou caracteres para a distância.")
  

  
        


