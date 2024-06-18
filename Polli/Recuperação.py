nota1 = float(input('Qual a nota do primeiro bimestre?'))
nota2 = float(input('qual a nota do segundo semestre?'))
média = (nota1 + nota2) / 2

if média >= 6:
    print('Parabéns!Você foi aprovada.')
elif média >= 3:
    print('Você fará recuperação.')

    recuperacao = float(input('qual a nota da recuperação?'))
    if recuperacao >= 7:
        print('Você foi aprovada!')
    else:
            print(' Você foi reprovada!')
else:
    print(' Você foi reprovada')


'''
Precisamos checar a nota do 1º bimestre e do 2º bimestre e fazer a média. Se a pessoa ficou de recuperação,
é necessário checar se tirou nota suficiente para passar. A regra é: A nota mínima de aprovação é 6. Se a aluna
tirou ao menos que 6, ela fica de recuperação, e abaixo de 3, ela está reprovada. Na recuperação, a nota mínima
de aprovação é 7.

Faça um programa que peça para a pessoa entrar com as duas notas de 0 a 10 e imprima se a aluna foi aprovada,
 reprovada ou está em recuperação. Se estiver em recuperação, peça para entrar com a nota da recuperação e imprima
   se foi aprovada ou reprovada.
'''