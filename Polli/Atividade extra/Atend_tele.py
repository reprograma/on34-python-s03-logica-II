entrada = int(input('Olá! Obrigada por ligar para nós! \nPara falar com Financeiro, digite 1.\nPara falar com Administrativo, digite 2. \nPara falar com Recursos Humanos, digite 3.\nPara falar com Assistência Técnica, digite 4.'))

if entrada == 1:
    print('Você será direcionada para o Financeiro.')
  
elif entrada == 2:
    print('Você será direcionada para o administrativo')
    
elif entrada == 3:
    print('Você será direcionada para o Recursos humanos')
    
else:
    print('Você será direcionada para a Assintência técnica')
Recado = input('você gostaria de deixar um recado para o setor, digite 1. Caso queira falar com atendente digite 2:')
if Recado == 1:
     print('Você pode deixar seu recado agora') 
else:
    print("Por favor, aguarde seu atendimento.")
    
 

print('fim')

'''


Bônus
Após ser direcionada para o departamento, pergunte: se a pessoa quer deixar um recado para o 
(nome do departamento) ou falar com atendente. caso a pessoa escolha deixar recado, imprima:
 "Você pode deixar seu recado agora". Caso ela escolha falar com atendente, imprima: "Por favor,
   aguarde seu atendimento".
'''