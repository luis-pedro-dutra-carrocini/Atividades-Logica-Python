#Escreva um algoritmo que receba 5 nomes em uma variável do tipo vetor. Depois escreva um relatório com os 5 nomes na memória.

nomes = []

for i in range(5):
    nome = input('Insira o nome: ')
    nomes.append(nome)

print('\nNomes Cadastrados:')
for i in range(5):
    print(nomes[i])