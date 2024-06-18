#Variáveis
salario = float(input('digite o seu salário:'))
vendas = float(input('digite o valor total das suas vendas:'))

#condições

if vendas <= 3000:
    comissão = (vendas * 0.1)
elif vendas <= 5000:
    comissão = (vendas * 0.15)
else:
    comissão = (vendas * 0.18)
total = salario + comissão
     
print('Este mês você receberá R$ {} de comissão, onde {} é a soma do salário com a comissão.' .format(comissão, total))
