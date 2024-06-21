# Interação com o usúario (input,infos)
print("Sistema de valores agência viagem maluca 😃🚌💺🎫🛄")
print("olá! Seja bem vinde, antes de prosseguirmos, diga seu nome")
nome_do_usuario = input (str("insira seu nome ✍️  :"))

print(f"{nome_do_usuario} que legal que queira viajar conosco!!")

print(f"Bom, senhor(a) {nome_do_usuario} segue a nossa tabela de viagem ")

print("Qualquer viagem tem um valor fixo R$ 20, porêm há adicionais ")


print ("Dito isso, insira quantos quilomêtros você vai viajar! ")



print("+==================+=================+")
print("| kms viajados     | valor por km     |")
print("+==================+=================+")
print("| Até 200km        | R$ 0,75          |")
print("| Até 500km        | R$ 0,60          |")
print("| Mais de 500km    | R$ 0,50          |")
print("+==================+=================+")
print ("Dito isso, insira quantos quilomêtros você vai viajar! ")


# input de kms e programação para úsuario inserir a classe correta 
try:
    valor_de_entrada = float (input("digite o km: "))

except ValueError:
    print ("Por favor, insira um número válido.")



# progrmação da excessão do <= 50, onde não conta
try:
 if valor_de_entrada <= 50:
    print ("poxa, não calculamos viagens com menos de 50km")
except:
        print ("Por favor, insira um número.")
        exit()

# caso o usuário insira números que não sejam inteiros ou strings, ele manda a mensagem 



# contagem de cada extra de porcentagem com cada km 
custo_fixo = 20.00

if valor_de_entrada <= 50:
    valor_por_km = 0.00

if valor_de_entrada <= 200:
    valor_por_km = 0.75

elif valor_de_entrada <= 50:
    valor_por_km = 0.00 
    print ("poxa, não calculamos viagens com menos de 50km")

elif valor_de_entrada <= 500:  
    valor_por_km = 0.60

elif valor_de_entrada > 500:  
    valor_por_km = 0.50 

# variáveis de soma 
custo_final = ( valor_de_entrada * valor_por_km + custo_fixo )

custo_menor_50 = (valor_de_entrada <= 50 * 0)


# a vizualização do usuário com o valor total e o km

try: 
    if valor_de_entrada <= 50:
        print(f"Sua viagem não tem soma seu km é {valor_de_entrada}")
except:
    print(f"Sua viagem com {valor_de_entrada} km custará R$ {custo_final}")


if valor_de_entrada > 50:
        print(f"Sua viagem com {valor_de_entrada} km custará R$ {custo_final}")
