#Faça um algoritmo que receba o nome de 5 alunos e 4 notas de 1 a 10 para cada um desses alunos. Calcule e escreva na tela a média dessas 4 notas para cada aluno. No final, escreva na tela quantos alunos tiveram média abaixo de 4, quantos tiveram média entre 4 e 5,99 e quantos tiveram média acima de 5,99.  

med4 = 0
med599 = 0
medac599 = 0

for i in range(5):
    input('\nInsira o Nome: ')
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))
    nota3 = float(input('Insira a terceira nota: '))
    nota4 = float(input('Insira a quarta nota: '))
    media  = round((nota1+nota2+nota3+nota4)/4)

    print(f'Média das notas: {media}')

    if (media < 4):
        med4 += 1
    elif (media > 4 and media <= 5.99):
        med599 += 1
    elif (media > 5.99):
        medac599 += 1

print(f'\nQuantidade de médias abaixo de 4: {med4}')
print(f'Quantidade de médias de 4 até 5,99: {med599}')
print(f'Quantidade de médias acima de 5,99: {medac599}')