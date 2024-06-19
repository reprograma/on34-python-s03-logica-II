##Adivinhe um número
#Neste programa, você precisa definir um número entre 1 e 100 e pedir para o 
# usuário tentar acertar. Você vai dizer se a pessoa acertou, chutou muito 
# alto ou chutou muito baixo. Diga qual o número.

#Atenção: esse programa só vai deixar a pessoa tentar acertar uma única vez. 
# Na próxima semana, você vai aprender a dar quantas tentativas quiser. 
# Esse curso só fica melhor! :D

numero_secreto = 5

print("Tente adivinhar o número secreto, vamos lá ! ")
tentativa = int(input("Digite um número de 1 a 100: "))

if tentativa == numero_secreto:
    print("Parabéns você acertou o número secreto !!!")
elif tentativa < numero_secreto:
    print("Que pena, você chutou baixo :( ...)")
    
else :
    print("Eita, você chutou alto '-'")