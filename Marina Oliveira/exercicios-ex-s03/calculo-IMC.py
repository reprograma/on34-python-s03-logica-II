print("***" "  VAMOS DESCOBRIR SEU IMC ?  " "***\n" )

def calcular_imc():
   
   nome = str(input("Por favor, digite seu nome: "))
   peso = float(input("Digite seu peso em kg: "))
   altura = float(input("Digite seu altura: "))

   imc = peso / (altura ** 2)

   if imc < 18.5:
      classificacao = "Magreza"

   elif imc <= 24.9:
      classificacao = "Normal"

   elif imc <= 29.9:
      classificacao = "Sobrepeso"

   elif imc <= 39.9:
       classificacao = "Obesidade"     

   else:
      classificacao = "Obesidade Grave"   

   print(f"Oi, {nome}! Sua classificação é {classificacao}.")

calcular_imc()          
       
