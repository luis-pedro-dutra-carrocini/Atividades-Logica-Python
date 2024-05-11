#Desenvolva um algoritmo que preencha o nome de três candidatos em um vetor de caractere [1..3] recebendo os nomes nas posições 1, 2 e 3 do vetor.
#Os números de voto dos candidatos serão respectivamente 1, 2 e 3 de acordo a sequência do cadastro. Portanto, se na posição 1 do vetor for cadastrado o candidato “X”, quando for executado o algoritmo, ao digitar 1 sabe-se que deverá incrementar + 1 na posição 1 da memória do vetor.
#Quando o usuário digitar 99, o algoritmo deverá sair do loop de votação e gerar o relatório.
#O relatório final deverá conter:
#1) o total de votos;
#2) os nomes dos respectivos candidatos, seguidos da quantidade de seus votos e percentual de votos do candidato diante do total geral de todos os votos.

cand = ['','Luís','Pedro','Dutra']
votcand = [0,0,0,0]
voto = 0
totvotos = 0

while (voto != 99):
    voto = int(input('\nInsira o número do Candidato: '))
    if (voto != 99):
        votcand[voto] += 1

        totvotos += 1

i = 1
while (i <= 3):
    print(f'{cand[i]} - {votcand[i]} votos - Porcentagem do votos: {round((votcand[i]*100)/totvotos)}%')
    i += 1