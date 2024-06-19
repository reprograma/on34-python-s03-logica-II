# nomear função
def calculo_viagem(kms):
    # colocando as condicoes dos valores da viagem
    if kms <= 200:
        valor_por_km = 0.75
    elif kms <= 500:
        valor_por_km = 0.60
    else:
        valor_por_km = 0.50

    valor_base = 20.00
    
    # operação matemática para calcular a função
    valor_total = valor_base + (kms * valor_por_km)
    return valor_total

print("Olá, seja bem-vinda. Esse programa irá calcular o preço da sua viagem de ônibus!")
# pedir ao usuário a quantidade de km da viagem
entrada = input("Digite a quantidade de quilômetros da viagem: ")
# colocar o formato que tem que ser
try:
     # converter a entrada para float
    kms = float(entrada)
    if kms > 0:
        valor_viagem = calculo_viagem(kms)

    
      # imprimir o resultado e corrigir os erros
        print("Sua viagem com", kms, "km custará R$", valor_viagem)
    else:
        print("Por favor, digite um número maior que zero.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número válido.")