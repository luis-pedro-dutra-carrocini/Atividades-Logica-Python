#Elabore um algoritmo que leia o nome e uma letra para representar o sexo de 5 pessoas e escreva na tela a quantidade de pessoas do sexo masculino e a quantidade de pessoas do sexo feminino. Caso o usuário digite uma letra diferente de M ou F, conte e apresente a quantidade como outras opções.

fem = 0
mas = 0
out = 0

for i in range(5):
    gen = input('\nInsira o gênero (F/M): ').upper()

    if (gen == 'F'):
        fem += 1
    elif (gen == 'M'):
        mas += 1
    else:
        out += 1

print(f'\nQuantidade do sexo Masculino: {mas}')
print(f'Quantidade do sexo Feminono: {fem}')
print(f'Quantidade de outro Sexo: {out}')