numero_secreto = 45

tentativa = int(input("Tente adivinhar o número q estou pensando! Você pode dá um palpite entre 1 e 100. Qual seu palpite? "))

if  numero_secreto == tentativa:
  print("Parabéns, você acertou!")
elif tentativa > numero_secreto:
  print ("Seu palpite está maior que o número que estou pensando!","O número que estava pensando era " , numero_secreto)
elif tentativa < numero_secreto:
  print ("Seu palpite está menor que o número que estou pensando!","O número que estava pensando era " , numero_secreto)
  
print("fim")