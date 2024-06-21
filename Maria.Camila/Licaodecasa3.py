print("Vamos viajar!!")

def validar_entrada():
    try:
        kms = float(input("Quantos kms você irá viajar? "))
        if kms < 50:
            print("A viagem deve ser de pelo menos 50 kms.")
            return validar_entrada()
        elif kms < 0:
            print("O número não pode ser negativo.")
            return validar_entrada()
        return kms
    except:
        print("Por favor, insira apenas números.")
        return validar_entrada()

def preco_viagem(kms):
    preco_base = 20.00
    if kms <= 200:
        preco_km = 0.75
    elif kms <= 500:
        preco_km = 0.60
    else:
        preco_km = 0.50

    valor_total = preco_base + (kms * preco_km)
    return valor_total

kms = validar_entrada()
total = preco_viagem(kms)
print(f"Sua viagem com {kms:.2f} km custará R$ {total:.2f}")

    
 
