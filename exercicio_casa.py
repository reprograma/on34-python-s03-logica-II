def preco_viagem():
    while True:
        try:
            print("Para começar, insira a quantidade de KM percorridos. Não são permitidos: \n⇨ Valores de KM menores que 50\n⇨ Inserir caracteres de texto na quilometragem\n⇨ Inserir número negativo")
            km = float(input("Quilometragem: "))

            if km < 50:
                print("\nO número que você digitou é menor do que 50, por gentileza informe uma quilometragem válida.")
                continue 

            if km <= 200:
                preco_km = 0.75
            elif km <= 500:
                preco_km = 0.60
            else:
                preco_km = 0.50

            preco_total = 20 + km * preco_km
            print("Sua viagem com", round(km, 2), "km custará R$", round(preco_total, 2), " onde ", round(km, 2), " é o número de quilômetros e ", round(preco_total, 2), "é o valor total a ser pago.")
            break 

        except:
            print("Entrada inválida. Por favor, digite um valor numérico maior ou igual a 50.")

preco_viagem()
