#Utilizando o comando enquanto, elabore um algoritmo que receba um determinado número inteiro na tela e escreva os múltiplos de 3 (3,6,9...) até que esse valor seja maior ou igual ao número lido (INCLUSIVE!). Se o número lido for menor que 3, somente escreva na tela: “informação Inválida”. . .

num = int(input('\nInsira o número: '))
cont = 3

if (num < 3):
    print('Informação Inválida!!!')
else:
    while (cont <= num):
        print(cont)
        cont += 3