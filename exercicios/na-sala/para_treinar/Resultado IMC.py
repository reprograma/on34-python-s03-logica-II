print ("Bem vindo a Calculadora de IMC\n") #\n cria uma linha logo abaixo

nome = input("Qual seu nome? " )
peso = float(input("Qual seu peso em quilos? "))
altura = float(input("Qual sua altura em metros (use ponto ao invés de vírgula? "))

imc = round(peso / (altura ** 2), 2) #ou imc = (peso / (altura * altura))

if imc <= 18.5:
    classificacao = "Magreza"
elif imc <= 24.9:
    classificacao = "Normal"
elif imc >= 29.9:
    classificacao = "Sobrepeso"
elif imc >= 39.9:
    classificacao = "Obesidade"
else:
    classificacao = "Obseidade grave"

print("Oi,", nome,"! Sua classificação é de", classificacao)