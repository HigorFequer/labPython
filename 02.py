## 1- Conversor de Moeda
## Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
## 
## * Valor em reais: R$ 100,00
## * Taxa do dólar: R$ 5,20
## * Taxa do euro: R$ 6,15
## O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro

print('Questão 1')
print(f'Valor em reais: R$ {valor_reais:.2f}')
print(f'Valor em dólares: $ {valor_dolares:.2f}')
print(f'Valor em euros: € {valor_euros:.2f}')
print()

## 2- Calculadora de Desconto
## Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
## 
## * Nome do produto: "Camiseta"
## * Preço original: R$ 50,00
## * Porcentagem de desconto: 20%
## O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

nome_produto = 'Camiseta'
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print('Questão 2')
print(f'Produto: {nome_produto}')
print(f'Preço original: R$ {preco_original:.2f}')
print(f'Desconto: {porcentagem_desconto}%')
print(f'Valor do desconto: R$ {valor_desconto:.2f}')
print(f'Preço final: R$ {preco_final:.2f}')
print()


## 3- Calculadora de Média Escolar
## Crie um programa que calcula a média escolar de um aluno. Use como seguintes notas:
## 
## * Nota 1: 7.5
## * Nota 2: 8.0
## * Nota 3: 6.5
## O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print('Questão 3')
print(f'Nota 1: {nota1:.2f}')
print(f'Nota 2: {nota2:.2f}')
print(f'Nota 3: {nota3:.2f}')
print(f'Média: {media:.2f}')
print()


## 4- Calculadora de Consumo de Combustível
## Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
## 
## * Distância percorrida: 300 km
## * Combustível gasto: 25 litros
## O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

distancia_percorrida = 300
combustivel_gasto = 25

consumo_medio = distancia_percorrida / combustivel_gasto

print('Questão 4')
print(f'Distância percorrida: {distancia_percorrida} km')
print(f'Combustível gasto: {combustivel_gasto} litros')
print(f'Consumo médio: {consumo_medio:.2f} km/l')