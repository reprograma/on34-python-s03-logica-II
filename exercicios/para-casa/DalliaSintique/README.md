# Entrega de atividade - Custo da Viagem

## **Ações realizadas**
- Realizado fork do repositório < https://github.com/reprograma/on34-python-s03-logica-II >
- Repositório remoto forkado < https://github.com/DalliaSintique/on34-python-s03-logica-II.git> clonado no repositório local.
- Criado a pasta DalliaSintique, dentro da pasta principal para a entrega da atividade.
- Criado os arquivos entrega_exercicio.py e README.md dentro da pasta DalliaSintique
- Segue o caminho da pasta: on34-python-s03-logica-II > exercicios > para-casa > DalliaSintique 
- Add e comitado as alterações. 
- Enviado as alterações para o repositório remoto (Push).
- Solicitado Pull Request.

## **Operações** 
Criado a função "custo_viagem", onde a mesma irá receber 3 operadores, que estão representados por (x,y,z).
A função deverá retornar com X somado a multiplicação de Y e Z. Conforme: return x + (y*z)

Para realizar o calculo, será necessário informar:
 1.  O valor fixo da viagem. Esta informação está armazenada na variável "custo_fixo".
 2.  O número de quilômetros que serão viajados. Esta informação é solicitada ao usuário através de input e armazenada na variável "km_viagem_desejada". Conforme: km_viagem_desejada = int(input("Digite aqui a quilometragem da viagem desejada, a partir de 50km:"))
 3. O valor em reais que será cobrado por quilômetro de acordo com a tabela abaixo:

| kms viajados |valor por km|
|Até 200km     |  R$ 0,75   |
|Até 500km     |  R$ 0,60   |
|Acima de 500km|  R$ 0,50   |

Dessa forma, ao chamar a função "custo_viagem", os valores que iremos atribuir aos operadores (x,y,z) serão: "custo_fixo" , "km_viagem_desejada" , valor por KM. 

Logo teremos: custo_fixo + ("km_viagem_desejada" * valor por KM)

* O custo total da viagem será impresso através if, elif e else.
* Utilizado Try e Except para orientar que o usuário não entre com letras, números negativos e caracteres especiais. 
