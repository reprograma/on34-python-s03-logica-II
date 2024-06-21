print("Análise do tempo")

temperatura = int(input("Qual a temperatura agora? "))

if temperatura > 27:
    print("Dia quente!")
elif temperatura >= 20:
    print("Dia agradável!")
else:
    print("Dia frio!")