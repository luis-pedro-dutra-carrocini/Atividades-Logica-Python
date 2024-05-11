#Elabore um algoritmo que receba o código, quantidade e preço unitário de 5 itens. A cada item digitado, calcule e mostre o preço calculado do item. No final escreva o valor total do pedido, baseado na soma dos totais dos intens.

totalfinal = 0

for i in range(5):
    cod = int(input('\nCódigo: '))
    quant = int(input('Quantidade: '))
    precouni = float(input('Preço Unitário: '))
    print(f'Total: {round(quant*precouni,2)}')

    totalfinal += quant*precouni

print(f'\nTotal do pedido: {round(totalfinal,2)}')