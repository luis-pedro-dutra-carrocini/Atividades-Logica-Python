#Um fazendeiro quer fazer um levantamento para descobrir entre seus bois, qual é o boi mais pesado e qual tem o menor peso. Para isso será necessário elaborar um algoritmo que leia o nome e o peso de todos esses animais. Ao final de cada registro, pergunte se o usuário deseja continuar, até que ele digite N. No corpo do algoritmo, faça a comparação dos pesos e no final escreva na tela qual é o boi mais pesado e qual é o boi de menor peso.

resp = 'S'
pesomaior = 0
nomemaior = ''
pesos = []
nomes = []

while (resp == 'S'):
    nome = input('\nNome do Boi: ')
    nomes.append(nome)

    peso = float(input('Peso do Boi: '))
    pesos.append(peso)

    if (peso > pesomaior):
        nomemaior = nome
        pesomaior = peso

    pesomenor = min(pesos)
    idmenor = pesos.index(pesomenor)
    
    nomemenor = nomes[idmenor]

    resp = input('Deseja continuar (S/N)? ').upper()

print(f'\nBoi mais Pesado: {nomemaior} - {pesomaior}Kg')
print(f'Boi menos Pesado: {nomemenor} - {pesomenor}Kg')