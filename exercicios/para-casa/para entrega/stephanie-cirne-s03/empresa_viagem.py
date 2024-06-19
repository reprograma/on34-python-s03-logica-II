print ("**************************************\n")

print ("🚚 Bem-vinda a empresa Leva Leva 🚚\n")

print ("**************************************\n")

print ("Digite o valor total de km da sua viagem e faça seu orçamento com a gente. Se liga nas regras ⬇️\n")

print ("🚫 Não fazemos viagens menores que 50km")
print ("❌ Não dê entrada com números negativos")
print ("⭕ Utilize apenas números. Beleza?\n")


def viagem (base,valor_km):
      
     try:
                
          km = float (input('Digite o valor de km da sua viagem: '))
                   
          if km < 0:
               print ("Por favor insira um número positivo")
               return
          
          if km < 50:
                print ("Por favor insira um valor acima de 50km")
                return
          
          if km >= 50 and km <= 200:
                  valor_km = 0.75

          elif km <= 500:
                  valor_km = 0.60

          elif km > 500:
                  valor_km =  0.50
                           
          viagem = base + km * valor_km

          return viagem

     except ValueError:
      print ("Digite um valor válido. Letras e caracteres não são aceitos")


base = 20
valor_km = 1

custo_viagem = viagem (base,valor_km)


if custo_viagem is not None:
       print ((f"O valor da viagem é de R$ {custo_viagem}"))







  

                 
