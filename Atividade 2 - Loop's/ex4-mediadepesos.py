#Faça um algoritmo que receba na tela o nome e o peso de uma quantidade de pessoas determinada pelo usuário. Após o loop escreva na tela a média do peso dessas pessoas.

quant = int(input('Quantas pessoas deseja verificar? '))
totalpeso = 0

print('\n--- Contagem Iniciada ---')
for i in range(quant):
    nome = input('\nInsira o nome: ')
    peso = float(input('Insira o peso: '))

    totalpeso += peso

print('\n--- Finalizada ---')
print(f'\nMédia dos pesos: {round((totalpeso/quant),2)}')