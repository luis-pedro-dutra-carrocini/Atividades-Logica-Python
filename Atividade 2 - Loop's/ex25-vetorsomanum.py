#Faça um programa que receba cinco números num vetor e mostre a saída a seguir conforme o modelo:
#Digite o  1º número : 5
#Digite o  2º número : 3
#Digite o  3º número : 2
#Digite o  4º número : 0
#Digite o  5º número : 2
#Os números digitados foram:
#5+ 3+ 2+ 0 + 2 = 12.

nums = []
formatacao = ''
soma = 0

for i in range(5):
    num = float(input(f'Digite o  {i+1}º número: '))
    nums.append(num)

    if (i != 0):
        formatacao = f'{formatacao} + {num}'
    else:
        formatacao = f'{num}'

    soma += num

print('\nOs números digitados foram:')
print(f'{formatacao} = {soma}')