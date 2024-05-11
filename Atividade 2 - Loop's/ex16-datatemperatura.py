#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia vários registros de ano, mês e dia (em variáveis do tipo int) e também uma temperatura para cada ano,mês,dia cadastrados. Informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas. 
#Exemplo:
#- Maior temperatura em: 05/11/2023 – 28.5
#- Menor temperatura em: 14/08/2023 – 13.2
#- Média das temperaturas: 24.3

resp = 'S'
datas = []
temps = []
maiortemp = 0
maiordata = ''
totaltemp = 0
qttemp = 0

while (resp == 'S'):
    print('\n-- Informe a Data --')
    dia = int(input('Dia: '))
    mes = int(input('Mês: '))
    ano = int(input('Ano: '))

    temp = int(input('Temperatura: '))
    temps.append(temp)

    data = f'{dia}/{mes}/{ano}'
    datas.append(data)

    menortemp = min(temps)
    idmenortemp = temps.index(menortemp)
    menordata = datas[idmenortemp]

    if (temp > maiortemp):
        maiortemp = temp
        maiordata = data

    qttemp += 1
    totaltemp += temp
    meidiatemp = totaltemp/qttemp

    resp = input('Deseja continuar (S/N)? ').upper()

print(f'\nMaior temperatura em: {maiordata} - {maiortemp}')
print(f'Menor temperatura em: {menordata} - {menortemp}')
print(f'Média das temperaturas: {round(meidiatemp,2)}')