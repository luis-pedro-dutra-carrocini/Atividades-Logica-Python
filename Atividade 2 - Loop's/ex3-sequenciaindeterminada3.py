#Desenvolva um algoritmo que receba dois valores inteiros de forma que o segundo valor digitado seja maior que o primeiro. Escreva na tela a sequência de valores, do primeiro até o segundo número digita, escrevendo na tela de  um em um. Ao final, escreva quantos números foram impressos na tela.

num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número (maior que o primeiro): '))
cont = 0

for i in range(num1, num2+1):
    print(i)
    cont += 1

print(f'\nQuantidade de números exibidos: {cont}')