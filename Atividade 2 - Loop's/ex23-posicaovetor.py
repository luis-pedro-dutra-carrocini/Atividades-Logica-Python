#Construa um algoritmo que receba valores para um vetor de 8 posições. Calcule e escreva na tela qual é o maior valor digitado no vetor e em qual posição está. Faça o mesmo para localizar o menor valor.

valores = []

for i in range(8):
    val = float(input(f'{i+1}° Valor: '))
    valores.append(val)

menorval = min(valores)
idmenor = valores.index(menorval)

maiorval = max(valores)
idmaior = valores.index(maiorval)

print(f'\nMaior valor: {idmaior+1}° Posição - {maiorval}')
print(f'Menor valor: {idmenor+1}° Posição - {menorval}')