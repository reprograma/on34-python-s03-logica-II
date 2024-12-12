print("Vamos brincar de Adivinhe o número!!")
numero = 75

numero_escolhido = float(input("Escolha um número de 0 a 100:"))

if numero == numero_escolhido:
    print("Parabéns! Você acertou o número.", numero)

elif numero_escolhido >= 85 and numero_escolhido < 100:
    print("Você passou perto!") 

elif numero_escolhido <= 65:
    print("Você chutou muito baixo.")

elif 76 <= numero_escolhido < 85:
  
    print("Você passou muito  perto!")
else:
    print("Você passou muito perto!")
