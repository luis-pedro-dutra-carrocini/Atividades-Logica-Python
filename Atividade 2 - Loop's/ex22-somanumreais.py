#Desenvolva um algoritmo que carregue um vetor com dez números reais e em seguida, faça:
#A) Calcule e mostre uma lista com a posição [i] e os respectivos números negativos (se houverem) . No final, mostre a quantidade de negativos.
#B) A posição (i) e os números positivos. No final, mostre a soma dos números positivos.

nums = []
qtnumneg = 0
qtzero = 0
somanumposi = 0

for i in range(10):
    num = float(input(f'Insira o {i+1}° número: '))
    nums.append(num)

print('\n-- Números Negativos --')
for i in range(10):
    if (nums[i] < 0):
        print(f'{i+1}° Número - {nums[i]}')
        qtnumneg += 1

if (qtnumneg == 0):
    print('\nNão há números negativos...')
else:
    print(f'\nQuantidade de números negativos: {qtnumneg}')

print('\n\n-- Números Positivos --')
for i in range(10):
    if (nums[i] > 0):
        print(f'{i+1}° Número - {nums[i]}')
        somanumposi += nums[i]

if (somanumposi == 0):
    print('\nNão há números positivos...')
else:
    print(f'\nSoma dos números positivos: {somanumposi}')

print('\n\n-- Números Neutros (0) --')
for i in range(10):
    if (nums[i] == 0):
        print(f'{i+1}° Número')
        qtzero += 1

if (somanumposi == 0):
    print('\nNão há números Neutros (0)...')
else:
    print(f'\nQuantidade de números Neutros: {qtzero}')