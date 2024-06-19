'''# Telemarketing
Você já deve ter ligado em uma empresa e ouvido uma lista de opções com números que deviam ser digitados com a
opção escolhida para ser direcionada a um certo departamento.
Seu trabalho agora é criar um minissistema de telemarketing. 

### Como vai funcionar?
O programa vai mostrar na tela as opções e, dependendo do número digitado, a pessoa vai ser direcionada a um outro
atendimento. Ao final, ficará assim:

Olá! Obrigada por ligar para nós
Para falar com Financeiro, digite 1.
Para falar com Administrativo, digite 2.
Para falar com Recursos Humanos, digite 3.
Para falar com Assistência Técnica, digite 4.

Dependendo da resposta, o programa vai mostrar na tela uma frase diferente. Por exemplo:
Ao responder 1, vai aparecer a frase:
***Você será direcionada para o Financeiro.***

### Bônus
Após ser direcionada para o departamento, pergunte: se a pessoa quer deixar um recado ou falar com atendente.
Caso a pessoa escolha deixar recado, imprima: "Você pode deixar seu recado agora".
Caso ela escolha falar com atendente, imprima: "Por favor, aguarde seu atendimento". 

### Bônus 2
Use funções ;)'''

def mostramenu():
  print("Olá! Obrigada por ligar para nós")
  print("Para falar com Financeiro, digite 1.")
  print("Para falar com Administrativo, digite 2.")
  print("Para falar com Recursos Humanos, digite 3.")
  print("Para falar com Assistência Técnica, digite 4.")

def escolhemenu():
  opcao = int(input("Digite a opção desejada "))
  if opcao == 1:
    print("Você será direcionada para o setor Financeiro ")
  elif opcao == 2:
    print("Você será direcionada para o setor Administrativo ")
  elif opcao == 3:
    print("Você será direcionada para o setor de Recursos Humanos ")
  elif opcao == 4:
    print("Você será direcionada para o setor de Assitencia Técnica ")
  
def escolhe_atend():
  opcao_dep = int(input("Se deseja deixar um recado, digite 1 ou falar com atendente, digite 2  "))
  if opcao_dep == 1:
    print("Você pode deixar seu recado agora")
  elif opcao_dep == 2:
    print("Por favor, aguarde seu atendimento")
    
mostramenu()
escolhemenu()
escolhe_atend()