#Faça um algoritmo que receba 15 valores inteiros. Aponte os números que se repetem e quantas vezes se repetem. Atenção para não repetir o mesmo número na lista de respostas.

numsrepeidos = []
qtrepetidas = []
numantigo = ''

for i in range(15):
    num = int(input(f'Insira o {i+1}° Número: '))

    if (num == numantigo):
        if (num in numsrepeidos):
            idnumrep = numsrepeidos.index(num)
            qtrepetidas[idnumrep] += 1
        else:
            numsrepeidos.append(num)
            qtrepetidas.append(2)

    numantigo = num

print('\n--- Números que se Repetem ---')
for i in range(len(numsrepeidos)):
    print(f'Número {numsrepeidos[i]} - Vezes inseridas: {qtrepetidas[i]}')