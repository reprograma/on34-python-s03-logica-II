print("Análise do tempo")

temperatura = float(input("Qual a temperatura agora? "))
escala = input("O numero digitado está em graus Celsius ou Farenheit? Digite C ou F: ")

if escala == "F":
    temperatura = (temperatura - 32) / 1.8

if temperatura > 25:
    print("Dia quente!")
elif temperatura > 15:
    print("Dia agradável!")
else:
    print("Dia frio!")