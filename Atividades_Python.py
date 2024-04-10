# Ler um número inteiro e exibir seu dobro.

numero = int(input(f'Digite um número intero: '))

print(f'O dobro de {numero} é: "{numero * 2}"')

# -----
# Exibir a multiplicação de dois números reais informados pelo usuário.

print(f'Digite dois números para serem multiplicados \n')

num_1 = float(input(f'Digite o primeiro número: '))
num_2 = float(input(f'Digite o segundo número: '))

print(f'{num_1} * {num_2} = {num_1 * num_2}')

# -----
# Calcular a média aritmética de três notas fornecidas pelo usuário.

nota_1 = float(input(f'Digite a primeira nota: '))
nota_2 = float(input(f'Digite a segunda nota: '))
nota_3 = float(input(f'Digite a terceira nota: '))

print(f'A média aritmética entre {nota_1}, {nota_2}, {nota_3} é: "{(nota_1 + nota_2 + nota_3) / 3}"')

# -----
# A imobiliária XYZ vende apenas terrenos retangulares. Faça um programa para ler as dimensões de um terreno e exibir a área do mesmo.

comprimento = float(input(f'Digite o comprimento do terreno: '))
largura = float(input(f'Digite a largura do terreno: '))

print(f'A área de um terreno de comprimento {comprimento} e largura {largura} é: "{comprimento * largura}"')

# -----
# Faça um programa para ler o salário de um funcionário e aumentá-lo em 20%. Imprima seu salário final.

salario = float(input(f'Digite o salário: '))

print(f'Um acréscimo de 20% num salário de {salario} é: "{salario * 1.2}"')

# -----
# Ler o valor de um cheque e escrever o quanto vai ser recolhido de CPMF. Considere que imposto recolhe uma taxa de 0,3%. Imprimir o valor do imposto.

cheque = float(input(f'Digite o valor do cheque: '))

print(f'O valor recolhido pelo CPMF de um cheque de valor {cheque} é: "{cheque * 0.3/100}"')

# -----
#Escreva uma sequência de comandos para solicitar o nome e a matrícula do aluno. Em seguida exibir as informações no seguinte formato:
# – Nome do Aluno: “XXXXXXXX”, Matrícula: “ZZZZ”

nome = str(input(f'Digite o nome do aluno: '))
matricula = int(input(f'Digite o número da matrícula: '))

print(f'- Nome do Aluno "{nome}", Matrícula: "{matricula}"')