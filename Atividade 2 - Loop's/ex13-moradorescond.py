#De acordo com as fichas de dados dos moradores de um condomínio, desenvolva um algoritmo que receba o nome, a quantidade de anos que o morador reside no condomínio e idade atual do morador. A cada registro, pergunte ao usuário se ele deseja continuar.
#No final, gere o relatório com os resultados:
#- Nome e idade do morador(a) responsável com maior idade;
#- Nome e tempo de residência do morador(a) responsável que reside no mesmo apartamento a mais tempo;
#- Quantidade geral de moradores cadastrados;
#- Média geral de idade dos moradores.

moradcad = 0
resp = 'S'
maioridade = 0
maiortempo = 0
somaidade = 0

while (resp == 'S'):
    nome = input('\nNome do Morador: ')
    temporesid = int(input('Quantidade de anos que reside no condomínio: '))
    idade = int(input('Idade do Morado: '))

    if (idade > maioridade):
        maioridade = idade
        nomemaioridade = nome

    if (temporesid > maiortempo):
        maiortempo = temporesid
        nomemaiortempo = nome

    moradcad += 1
    somaidade += idade

    resp = input('\nDeseja continuar o registro (S/N)? ').upper()

print(f'\nMorador com o maior tempo de residencia: {nomemaiortempo} - {maiortempo} anos')
print(f'Morador com maior idade: {nomemaioridade} - {maioridade} anos')
print(f'Quantidade geral de moradores: {moradcad}')
print(f'Média de idade dos Moradores: {round(somaidade/moradcad,2)} anos')