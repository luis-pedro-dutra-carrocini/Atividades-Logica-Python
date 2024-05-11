#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

erro = 'S'
while (erro == 'S'):
    nota = float(input('\nInsira a nota: '))

    if (nota >= 0 and nota <= 10):
        print('Nota válida!!!')
        erro = 'N'
    else:
        print('Nota Inválida!!!')