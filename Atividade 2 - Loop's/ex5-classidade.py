#Elabore um algoritmo que entre com o nome e idade de 5 pessoas. Se a idade for maior que 70, escreva na tela: “Idoso”. Se a idade for menor que 14, escreva: “Criança” para cada um dos registros inseridos. No final, apresente: o total de idosos, o total de crianças e o total de pessoas com idade que não se enquadra nessas duas condições.

idoso = 0
crianca = 0
outro = 0

for i in range(5):
    idade = int(input('\nInsira a idade: '))

    if (idade > 70):
        print('Idoso')
        idoso += 1
    elif (idade < 14):
        print('Criança')
        crianca += 1
    else:
        print('Não se enquadra em nenhuma idade')
        outro += 1

print(f'\nTotal de Idosos: {idoso}')
print(f'Total de Crianças: {crianca}')
print(f'Outras Idades: {outro}')