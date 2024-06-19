print("Olá,seja bem vindo(a) ao viajafácil, calcule sua viagem!")


try:
    viagem_km = float(input("Olá por favor,digite quantos Km tem sua viagem: "))


    if viagem_km < 0:
        print("Olá por favor, digite valores válidos!")
    elif viagem_km < 50:
        print("Olá,sua viagem não pode ter menos de 50km, por favor digite uma quilometragem válida")
    elif viagem_km <= 200:
        valor_viagem = (viagem_km * 0.75) + 20.00
        print(f"Sua viagem com {viagem_km}kms custará R$ {valor_viagem}")
    elif viagem_km <= 500:
        valor_viagem = (viagem_km * 0.60) + 20.00
        print(f"Sua viagem com {viagem_km}kms custará R$ {valor_viagem}")
    else:
        valor_viagem = (viagem_km * 0.50) + 20.00
        print(f"Sua viagem com {viagem_km}kms custará R$ {valor_viagem}")


except :
    print("Por favor, digite valores válidos!")




