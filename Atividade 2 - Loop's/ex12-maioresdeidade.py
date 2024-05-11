#Faça um algoritmo que receba o nome e a idade de 5 pessoas, escreva na tela a quantidade de pessoas maiores de idade (>=18) e a quantidade de menores.  Apresente o nome e a idade da pessoa com a menor idade de todos.

qtmaior = 0
qtmenor = 0
cont = 1

while (cont <= 5):
    idade = int(input('\nInsira a idade: '))

    if (idade < 1):
        print('Idade Inválida!!')
    else:
        cont += 1
        if (idade < 18):
            qtmenor += 1
        elif (idade >= 18):
            qtmaior +=1

print(f'\nQuantidade de Maiores de 18 anos: {qtmaior}')
print(f'Quantidade de Menores de 18 anos: {qtmenor}')