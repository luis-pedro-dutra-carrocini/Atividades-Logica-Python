#Crie um algoritmo que leia a idade de 10 atletas.  
#De acordo com a tabela, o Algoritmo deverá escrever os seguintes resultados.
#- A quantidade de pessoas enquadradas em cada categoria;
#- A média de idade de cada categoria;
#- A média de idade geral de todas as idades.

qtinfantil = 0
qtjuvenil = 0
qtadulto = 0
qtidoso = 0

sominfantil = 0
somjuvenil = 0
somadulto = 0
somidoso = 0
i = 1

while (i <= 10):
    idade = int(input('\nInsira a Idade do Atleta: '))

    if (idade < 1):
        print('Idade Inválida!!')
    else:
        i += 1
        if (idade < 13):
            qtinfantil += 1
            sominfantil += idade
        elif (idade < 18):
            qtjuvenil += 1
            somjuvenil += idade
        elif (idade < 60):
            somadulto += idade
            qtadulto += 1
        elif (idade > 60):
            qtidoso += 1
            somidoso += idade

mediageral = (somadulto+somidoso+sominfantil+somjuvenil)/10

print('\n--- Quantidade por Categoria ---')
print(f'Infantil: {qtinfantil}')
print(f'Juvenil: {qtjuvenil}')
print(f'Adulto: {qtadulto}')
print(f'Idoso: {qtidoso}')

print('\n--- Média de Idade por Categoria ---')
print(f'Infantil: {round(sominfantil/qtinfantil,2)}')
print(f'Juvenil: {round(somjuvenil/qtjuvenil,2)}')
print(f'Adulto: {round(somadulto/qtadulto,2)}')
print(f'Idoso: {round(somidoso/qtidoso,2)}')

print(f'\nMédia Geral das Idades: {round(mediageral,2)}')