#Faça um algoritmo usando vetores que recebam o nome e a nota de oito alunos. 
#Calcule apresente um relatório com:
#A) A média da sala
#B) Lista com nome e nota dos alunos acima da média da sala
#C) Lista com nome e nota dos alunos abaixo da média da sala
#D) Escreva o nome e a nota do aluno com a maior nota da turma

alunos = []
notas = []
totalnotas = 0

for i in range(8):
    nome = input('\nNome do Aluno: ')
    alunos.append(nome)

    nota = float(input('Nota do Aluno: '))
    notas.append(nota)

    totalnotas += nota

media = totalnotas/8
print(f'\nMédia de nota da Sala: {round(media,2)}')

print('\n--- Alunos acima da média ---')
for i in range(8):
    if (notas[i] > media):
        print(f'{alunos[i]} - {notas[i]}')

print('\n\n--- Alunos abaixo da média ---')
for i in range(8):
    if (notas[i] < media):
        print(f'{alunos[i]} - {notas[i]}')

print('\n\n--- Alunos na média ---')
for i in range(8):
    if (notas[i] == media):
        print(f'{alunos[i]} - {notas[i]}')

maiornota = max(notas)
idmaiornota = notas.index(maiornota)
nomemaior = alunos[idmaiornota]

print(f'\nAluno com Maior Nota: {nomemaior} - {maiornota}')