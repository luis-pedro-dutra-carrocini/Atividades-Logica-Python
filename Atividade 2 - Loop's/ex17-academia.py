#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados será quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também devem ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.

codigo = 1
maiorpeso = 0
maioraltura = 0
codigos = []
pesos = []
alturas = []

while (codigo != 0):
    codigo = int(input('\nInsira o código: '))

    if (codigo != 0):
        codigos.append(codigo)
        altura = float(input('Insira a altura: '))
        alturas.append(altura)
        peso = float(input('Insira o peso: '))
        pesos.append(peso)

        if (altura > maioraltura):
            maioraltura = altura
            codmaioralt = codigo

        if (peso > maiorpeso):
            maiorpeso = peso
            codmaiorpeso = codigo
        
        menoraltura = min(alturas)
        idmenoraltura = alturas.index(menoraltura)
        codmenoraltura = codigos[idmenoraltura]

        menorpeso = min(pesos)
        idmenorpeso = pesos.index(menorpeso)
        codmenorpeso = codigos[idmenorpeso]

print(f'\nCliente mais alto: {codmaioralt} - {maioraltura} metros')
print(f'Cliente mais baixo: {codmenoraltura} - {menoraltura} metros')
print(f'Cliente mais gordo: {codmaiorpeso} - {maiorpeso} Kg')
print(f'Cliente mais magro: {codmenorpeso} - {menorpeso} Kg')