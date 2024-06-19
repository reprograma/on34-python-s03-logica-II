print("^^^ " "COMO ESTÁ O TEMPO HOJE?" " ^^^\n")


temperatura = float(input("Digite a temperatura atual em graus Celsius: "))

if temperatura > 27:
    classificacao = "dia quente"

elif temperatura >= 20:
    classificacao = "dia agradável"

else:
    classificacao =  "dia frio"

print(f"O dia está classificado como {classificacao}.")

