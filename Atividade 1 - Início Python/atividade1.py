#Problema 1;
nome = input('Insira o Nome: ')
idade = int(input('Insira a Idade: '))

if (idade > 17):
  print(f'{nome}, está apto para tirar a carteira de motorista, idade: {idade} anos.')
else:
  idade_restante = 18 - idade
  if (idade_restante > 1):
    print(f'{nome}, fatam {idade_restante} anos para tirar sua carteira, idade: {idade} anos.')
  else:
    print(f'{nome}, fata {idade_restante} ano para tirar sua carteira, idade: {idade} anos.')


#Problema 2;
a = float(input('Valor de A: '))
b = float(input('Valor de B: '))

c = b
b = a
a = c

print(f'Valor de A: {a}; Valor de B: {b}')


#Problema 3;
tipo_com = input('Insira o Tipo de Combustível, Álcool = (A) Gasolina = (G): ').upper()
qtkm_comb = float(input('Quantidade de Km que o carro anda por litro: '))
qtkm_percorridos = float(input('Quantidade de Km que serão percorridos: '))
qt_litrosgasto = qtkm_percorridos / qtkm_comb

if (tipo_com == 'G'):
  val_gasto = qt_litrosgasto * 5.10
  print(f'Quantidade de litros gasto: {qt_litrosgasto}; Valor que será gasto: {val_gasto}')
elif (tipo_com == 'A'):
  val_gasto = qt_litrosgasto * 3.45
  print(f'Quantidade de litros gasto: {qt_litrosgasto}; Valor que será gasto: {val_gasto}')
else:
  print('Tipo de combutível não definido, tente novamente...')


#Problema 4;
d = int(input('Dia: '))
m = int(input('Mês: '))
a = int(input('Ano: '))

# Adicionei o IF por causa da formatação
# Sem ele a data poderia ficar EX: 3/3/2024 
# Ou seja não haveria o 0 antes dos números menores que 10, no dia e no mês
if (d < 10) and (m < 10):
  print(f'0{d}/0{m}/{a}')
elif (d < 10):
  print(f'0{d}/{m}/{a}')
elif (m < 10):
  print(f'{d}/0{m}/{a}')
else:
  print(f'{d}/{m}/{a}')


#Problema 5;
val_com = float(input('Valor da Compra: '))

if (val_com > 100):
  des = val_com * 0.1
else:
  des = 0

val_comfi = val_com - des

print(f'Valor do Desconto: {des}; Valor da compra Final: {val_comfi}')


#Problema 6;
nomec1 = input('Insira o Nome do 1° Candidato: ')
nomec2 = input('Insira o Nome do 2° Candidato: ')
votosc1 = int(input(f'Quantidade de Votos {nomec1}: '))
votosc2 = int(input(f'Quantidade de Votos {nomec2}: '))

votosto = votosc1 + votosc2

percv1 = (votosc1*100)/votosto
percv2 = (votosc2*100)/votosto

if (votosc1 > votosc2):
  print(f'O candidato {nomec1} foi o primeiro colocado, obtendo a votação: {votosc1}, representando {percv1}% dos votos.')
  print(f'O candidato {nomec2} foi o segundo colocado, obtendo a votação: {votosc2}, representando {percv2}% dos votos.')
elif (votosc2 > votosc1):
  print(f'O candidato {nomec2} foi o primeiro colocado, obtendo a votação: {votosc2}, representando {percv2}% dos votos.')
  print(f'O candidato {nomec1} foi o segundo colocado, obtendo a votação: {votosc1}, representando {percv1}% dos votos.')
else:
  print(f'Ouve um empate, a porcentagem de votos de ambos os candidatos é 50%')


#Problema 7;
nome = input('Insira o Nome do Empregado: ')
sal = float(input('Insira o seu salário: '))

if (sal > 5000):
  aumento = sal*0.05
  perau = 5
else:
  aumento = sal*0.10
  perau = 10

novo_sal = sal+aumento
print(f'O {nome}, salário {sal}, entrou na fiaxa de {perau}% de aumento e o salário passou de {sal} para {novo_sal}.')


#Problema 8;
med1 = float(input('Insira a media da 1° Disciplina: '))
med2 = float(input('Insira a media da 2° Disciplina: '))
med3 = float(input('Insira a media da 3° Disciplina: '))
med4 = float(input('Insira a media da 4° Disciplina: '))
med5 = float(input('Insira a media da 5° Disciplina: '))
9
media = (med1+med2+med3+med4+med5)/5

if (media > 9):
  print(f'O aluno receberá uma menção de destaque, média total: {media}')
else:
  print(f'O aluno não receberá uma menção de destaque, média total: {media}')


#Problema 9;
med1 = float(input('Insira a media da 1° Disciplina: '))
med2 = float(input('Insira a media da 2° Disciplina: '))
med3 = float(input('Insira a media da 3° Disciplina: '))
med4 = float(input('Insira a media da 4° Disciplina: '))
med5 = float(input('Insira a media da 5° Disciplina: '))
9
media = (med1+med2+med3+med4+med5)/5

if (media > 9):
  print(f'O aluno receberá uma menção de destaque, média total: {media}')
else:
  print(f'O aluno não receberá uma menção de destaque, média total: {media}')


#Problema 10;
valcom = float(input('Insira o Valor da Compra: '))
indicou = input('indicou um novo Cliente Sim(S) Não(N): ').upper()

if (indicou == 'S'):
  des = valcom*0.15
  valpag = valcom - des
  print(f'O cliente receberá 15% de desconto, por ter indicado um cliente, valor a pagar: {valpag}')
else:
  print(f'O cliente não receberá 15% desconto, pois não indicou um cliente, valor a pagar: {valcom}')


#Problema 11;
valcom = float(input('Insira o Valor da Compra: '))
indicou = input('indicou um novo Cliente Sim(S) Não(N): ').upper()

if (indicou == 'S'):
  des = valcom*0.15
  valpag = valcom - des
  print(f'O cliente receberá 15% de desconto, por ter indicado um cliente, valor a pagar: {valpag}')
else:
  print(f'O cliente não receberá 15% desconto, pois não indicou um cliente, valor a pagar: {valcom}')


#Problema 12;
valcom = float(input('Insira o Valor da Compra: '))

if (valcom > 200):
  frete = 'Gratis'
  valto = valcom
else:
  frete = valcom*0.1
  valto = valcom+frete

print(f'Valor da Compra: {valcom}; Valor do Frete: {frete}; Valor Total: {valto}')