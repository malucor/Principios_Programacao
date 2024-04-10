# Ler um número inteiro de dizer se é par ou ímpar.

numero = int(input(f'Digite um número inteiro: '))

if (numero % 2) == 0:
  print(f'O número {numero} é par')
else:
  print(f'O número {numero} é ímpar')

# -----
# Ler a temperatura de uma pessoa e exibir a mensagem “Febre Alta” (temp ≥ 39), “Febril” (39 > temp ≥ 37) ou “Sem Febre” (temp < 37).

temperatura = float(input(f'Digite a temperatura: '))

if temperatura >= 39:
  print(f'{temperatura} = "Febre Alta"')
elif 39 > temperatura >= 37:
  print(f'{temperatura} = "Febril"')
else:
  print(f'{temperatura} = "Sem Febre"')

# -----
# Entrar com um distância (km) e o tempo de viagem (horas) de um automóvel, e dizer se a velocidade média foi superior ao limite (110 km/h) ou não.

distancia = float(input(f'Digite a distância, em Km: '))
tempo = float(input(f'Digite o tempo, em horas: '))

velocidade = distancia / tempo

if velocidade > 110:
  print(f'A velocidade média de uma viagem de {distancia} Km feita em {tempo} horas foi superior ao limite\n{velocidade} Km/h > 110 Km/h')
else:
  print(f'A velocidade média de uma viagem de {distancia} Km feita em {tempo} horas foi inferior ou igual ao limte\n{velocidade} Km/h <= 110 Km/h')

# -----
# Faça um Programa que peça para entrar com um ano (inteiro com 4 dígitos) e determine se o mesmo é ou não bissexto (divisível por 4).

ano = int(input(f'Digite um ano (com 4 dígitos): '))

if ano % 4 == 0:
  print(f'O ano {ano} é bissexto')
else:
  print(f'O ano {ano} não é bissexto')

# -----
# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num_1 = float(input(f'Digite o primeiro número: '))
num_2 = float(input(f'Digite o segundo número: '))
num_3 = float(input(f'Digite o terceiro número: '))

if num_1 >= num_2 and num_2 >= num_3:
  print(f'{num_1} >= {num_2} >= {num_3}')
elif num_1 >= num_3 and num_3 >= num_2:
  print(f'{num_1} >= {num_3} >= {num_2}')
elif num_2 >= num_1 and num_1 >= num_3:
  print(f'{num_2} >= {num_1} >= {num_3}')
elif num_2 >= num_3 and num_3 >= num_1:
  print(f'{num_2} >= {num_3} >= {num_1}')
elif num_3 >= num_1 and num_1 >= num_2:
  print(f'{num_3} >= {num_1} >= {num_2}')
elif num_3 >= num_2 and num_2 >= num_1:
  print(f'{num_3} >= {num_2} >= {num_1}')

# -----
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco_1 = float(input(f'Digite o primeiro preço: '))
preco_2 = float(input(f'Digite o segundo preço: '))
preco_3 = float(input(f'Digite o terceiro preço: '))

if preco_1 <= preco_2 and preco_1 <= preco_3:
  print(f'É para comprar o produto de preço {preco_1}')
elif preco_2 <= preco_1 and preco_2 <= preco_3:
  print(f'É para comprar o produto de preço {preco_2}')
elif preco_3 <= preco_1 and preco_3 <= preco_2:
  print(f'É para comprar o produto de preço {preco_3}')

# -----
# Faça um Programa que pergunte em que turno a pessoa estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print(f'M - Matutino\nV - Vespetino\nN - Noturo')

turno = str(input(f'Digite o turno: '))

if turno == 'M' or turno == 'm':
  print(f'"Bom Dia!"')
elif turno == 'V' or turno == 'v':
  print(f'"Boa Tarde!"')
elif turno == 'N' or turno == 'n':
  print(f'"Boa Noite!"')
else:
  print(f'"Valor Inválido!"\n\nFoi digitado "{turno}", mas só é aceito M, V ou N')

# -----
# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print(f'obs: Considere que a semana começa no Domingo\n')

dia = int(input(f'Digite o número correspondente ao dia da semana:'))

if dia == 1:
  print(f'Domingo')
elif dia == 2:
  print(f'Segunda-feira')
elif dia == 3:
  print(f'Terça-feira')
elif dia == 4:
  print(f'Quarta-feira')
elif dia == 5:
  print(f'Quinta-feira')
elif dia == 6:
  print(f'Sexta-feira')
elif dia == 7:
  print(f'Sábado')
else:
  print(f'"Valor Inválido!"\n\nFoi digitado "{turno}", mas só é aceito valores de 1 a 7')