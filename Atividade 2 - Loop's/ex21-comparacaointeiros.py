#Faça um algoritmo em que o usuário passe os dados:
#A) Um número inteiro para comparação.
#B) Vetor com 15 elementos inteiros. 
#Após a entrada de todos os números do vetor, verifique e escreva os elementos maiores ou iguais ao número de comparação digitado pelo usuário, escrevendo na tela as posições em que esses elementos se encontram, seguidas de seus respectivos valores.

num = int(input('\nNúmero inteiro para a comparação: '))
print('')
elementos = []

for i in range(15):
    elem = int(input(f'{i+1}° Elemento inteiro: '))
    elementos.append(elem)

print('\n-- Elementos (>=) ao Número de Comparação --')
for i in range(15):
    exibielem = elementos[i]
    if (exibielem >= num):
        print(f'{i+1}° Elemento - {exibielem}')