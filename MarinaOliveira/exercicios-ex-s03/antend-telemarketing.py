print("Bem-vinda a agência Reprograma, obrigada por ligar para nós. \nPara falar com Financeiro, digite 1.")
print("Para falar com Administrativo, digite 2. \nPara falar com Recursos Humanos, digite 3.")
print("Para falar com Assistência Técnica, digite 4.")

resposta= int(input("Escolha as opções de 1 ao 4: "))

if resposta == 1:
    print("Você será direcionada para o Financeiro.")
    recadofin = int(input("Você quer deixar um recado para o Financeiro (1) ou falar com o atendente (2)? "))
    if recadofin == 1:
      print("Você pode deixar seu recado agora: ")
    elif recadofin == 2:
      print("Por favor, aguarde seu atendimento.")
    else:
      print("Opção inválida.")     
elif resposta == 2:
    print("Você será direcionada para o Administrativo.")
    recadoadm = int(input("Você quer deixar um recado para o Administrativo (1) ou falar com o atendente (2)? "))
    if recadoadm == 1:
      print("Você pode deixar seu recado agora: ")
    elif recadoadm == 2:
        print("Por favor, aguarde seu atendimento.")
    else:
        print("Opção inválida. Estamos encerrando o atendimento.")
elif resposta == 3:
    print("Você será direcionada para o Recursos Humanos.")
    recadorh = int(input("Você quer deixar um recado para o Recursos Huumanos (1) ou falar com o atendente (2)? "))
    if recadorh == 1:
        print("Você pode deixar seu recado agora: ")
    elif recadorh == 2:
       print("Por favor, aguarde seu atendimento.")
    else:
        print("Opção inválida. Estamos encerrando o atendimento.")
elif resposta == 4:
    print("Você será direcionada para a Assistência Técnica.")
    recadotec = int(input("Você quer deixar um recado para a Assistência Técnica (1) ou falar com o atendente (2)? "))
    if recadotec == 1:
       print("Você pode deixar seu recado agora: ")
    elif recadotec == 2:
        print("Por favor, aguarde seu atendimento.")
    else:
        print("Opção inválida. Estamos encerrando o atendimento.")
else:
    print("Opção inválida. Estamos encerrando o atendimento.")