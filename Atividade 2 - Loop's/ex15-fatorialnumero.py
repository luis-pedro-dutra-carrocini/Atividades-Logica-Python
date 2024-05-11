#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 55! =  5 . 4 . 3 . 2 . 1 = 120

num = int(input('Insira o número: '))
cont = num
result = num
formatacao = ''

while (cont >= 1):
    cont -= 1
    if (cont != 0):
        result = result*(cont)

    if (cont != 0):
        formatacao = f'{formatacao} {(cont+1)} .'
    else:
        formatacao = f'{formatacao} {(cont+1)}'

print(f'Fatorial de: {num}! =  {formatacao} = {result}')