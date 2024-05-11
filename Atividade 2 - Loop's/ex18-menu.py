#De acordo com esta interface, elabore um algoritmo que primeiramente escreva as linhas na tela: 
#1 – Tabuada; 2 – Cálculo do Produto; 3 – Sequência de Números. 9 – Sair. 
#Para cada opção escolhida, execute o algoritmo conforme enunciados abaixo:
#1 - Tabuada: Receber um número e executar um loop para que escreva a tabuada do valor digitado;
#2 – Cálculo: Elabore um algoritmo que receba o código, quantidade e preço unitário de 5 itens. A cada item digitado, calcule e mostre o preço calculado do item. No final escreva o valor total do pedido, baseado na soma dos totais dos intens.  
#3 – Sequência: Desenvolva um algoritmo que receba dois valores inteiros de forma que o segundo valor digitado seja maior que o primeiro. Escreva na tela a sequência de valores, do primeiro até o segundo número digita, escrevendo na tela de um em um. Ao final, escreva quantos números foram impressos na tela.
#9 – Sair: Condição While para sair da execução.

op = 0
while (op != 9):
    print('\n--- Opções do Menu ---')
    print('1 – Tabuada \n2 – Cálculo do Produto \n3 – Sequência de Números \n9 – Sair')
    op = int(input('Escolha uma opção: '))

    if (op == 1):
        num = int(input('\nInsira o número que deseja fazer a tabuada: '))
        for i in range(10):
            print(f'{num} x {i+1} = {num*(i+1)}')
    
    elif (op == 2):
        valtotal = 0
        for i in range(5):
            cod = int(input('\nInsira o código do produto: '))
            qt = int(input('Quantidade: '))
            precouni = float(input('Preço unitário em R$: '))

            print(f'Valor: R$ {precouni*qt}')
            valtotal += precouni*qt

        print(f'\nValor total a pagar: R$ {valtotal}')

    elif (op == 3):
        num1 = int(input('\nInsira o 1° número: '))
        num2 = int(input('Insira o 2° número (Maior que o primeiro): '))

        if (num1 >= num2):
            print('Número inválido - 2° Número tem que ser maior que o 1°')
        else:
            qtnumdig = 0
            while (num1 <= num2):
                print(num1)
                num1 += 1
                qtnumdig += 1

            print(f'\nQuantidade de números exibidos: {qtnumdig}')