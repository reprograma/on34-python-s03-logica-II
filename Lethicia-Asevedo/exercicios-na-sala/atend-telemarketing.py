#Telemarketing
#Você já deve ter ligado em uma empresa e ouvido uma lista de opções com números
# que deviam ser digitados com a opção escolhida para ser direcionada a um certo
# departamento. Seu trabalho agora é criar um minissistema de telemarketing.

#Como vai funcionar?
#O programa vai mostrar na tela as opções e, dependendo do número digitado, a pessoa 
# vai ser direcionada a um outro atendimento. Ao final, ficará assim:

#Olá! Obrigada por ligar para nós Para falar com Financeiro, digite 1. 
# Para falar com Administrativo, digite 2. Para falar com Recursos Humanos, digite 3. 
# Para falar com Assistência Técnica, digite 4.

#Dependendo da resposta, o programa vai mostrar na tela uma frase diferente. 
# Por exemplo: Ao responder 1, vai aparecer a frase: Você será direcionada para o Financeiro.

#Bônus
#Após ser direcionada para o departamento, pergunte: se a pessoa quer deixar um recado 
# ou falar com atendente. Caso a pessoa escolha deixar recado, imprima: 
# "Você pode deixar seu recado agora". Caso ela escolha falar com atendente, 
# imprima: "Por favor, aguarde seu atendimento".

#Bônus 2
#Use funções ;)

print("Bem vindo a nossa central de atendimento")

print ("Esolha a opção do setor com quem deseja entrar em contato: ")

print("""

    1 - FINANCEIRO\n
    2 - ADMINISTRATIVO\n
    3 - RECURSOS HUMANOS\n
    4 - ASSISTÊNCIA TÉCNICA
      
      """)

financeiro = 1
administrativo = 2
recursos_humanos = 3
assistencia_tecnica = 4

opcao_escolhida = int(input("Digite aqui o número da opção escolhida: "))

if opcao_escolhida == 1:
    print("Você será direcionado(a) para o setor Financeiro, aguarde...")

elif opcao_escolhida == 2:
    print("Você será direcionado(a) para o setor Administrativo, aguarde...")

elif opcao_escolhida == 3:
    print("Você será direcionado(a) para o setor de Recursos Humanos, aguarde...")

elif opcao_escolhida == 4:
    print("Você será direcionado(a) para o setor da Assistência Técnica, aguarde...")

opcao_escolhida2 = int(input(print("""Você deseja deixar um recado para o departamento ou falar com um de nossos atendentes?\n
      
      Responda 1 para deixar um recado:\n
      Responda 2 para falar com um de nossos atendentes:

      """)))

if opcao_escolhida2 == 1:
    str(input(print("Escreva aqui a sua mensagem: ")))
    print("""Obrigado pelo recado, nosso setor irá retornar no prazo de 24hrs.
          Para mais informções entre em contato com um de nossos atendentes""")
else :
    print("Por favor, em instantes você será atendido, aguarde...")