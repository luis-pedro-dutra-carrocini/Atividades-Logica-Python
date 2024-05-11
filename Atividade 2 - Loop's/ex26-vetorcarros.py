#Desenvolva um programa que o usuário cadastre um vetor com os modelos de cinco carros (exemplo de modelos: Onix, Creta, Mobi etc.). Carregue um outro vetor com o consumo desses carros, indicando quantos quilômetros o carro roda com um litro de combustível.
#Após cadastrar os carros e seus gastos, calcule e mostre: 
#- O modelo do carro mais econômico e a sua quantidade de Km\Lt.
#- Qual posição do vetor este carro mais econômico se encontra.
#- Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1.000 quilômetros.

modelos = []
rodagens = []
maiorkm = 0

for i in range(5):
    modelo = input(f'\n{i+1}° Modelo: ')
    modelos.append(modelo)

    rodagem = float(input(f'Quantos quilômetros ele anda com 1 Litro: '))
    rodagens.append(rodagem)

    if (rodagem > maiorkm):
        maiorkm = rodagem
        modelomaiorkm = modelo
        posmaiorkm = i+1

print(f'\nCarro mais econômico: {posmaiorkm}° Modelo - {modelomaiorkm} - {maiorkm} Km\Lt')

print('\n--- Consumo de combistivel para a rodagem de 1.000 Km ---')
for i in range(5):
    print(f'{i+1}° Modelo - {modelos[i]} - {round(1000/rodagens[i],2)} Litros')