'''
Crie um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

- Quantas pessoas foram cadastradas;
- Uma listagem com as pessoas mais pesadas;
- Uma listagem com as pessoas mais leves.
'''

cadastro = []

while True:
    cadastro.append(input('Digite o nome: ').strip())
    cadastro.append(float(input('Digite o peso: kg ')))
    continuar = ' '
    
    while continuar not in 'SN':
        continuar = input('Deseja continuar com o cadastro? [S/N] ').strip().upper()[0]
    
    if continuar == 'N':
        break

print('\n' + '-=' * 30 + '-')
print(f'Os dados cadastrados foram {cadastro}.')
print(f'Foram cadastradas {int(len(cadastro) / 2)} pessoas.')

mais_pesada = []
mais_leve = []

for valor in range(0, len(cadastro), 2):
    if valor == 0:
        mais_pesada.append(cadastro[valor + 0])
        mais_pesada.append(cadastro[valor + 1])
        mais_leve.append(cadastro[valor + 0])
        mais_leve.append(cadastro[valor + 1])
    else:
        if mais_pesada[-1] < cadastro[valor + 1]:
            mais_pesada.clear()
            mais_pesada.append(cadastro[valor + 0])
            mais_pesada.append(cadastro[valor + 1])
        elif mais_pesada[-1] == cadastro[valor + 1]:
            mais_pesada.append(cadastro[valor + 0])
            mais_pesada.append(cadastro[valor + 1])
            
        if mais_leve[-1] > cadastro[valor + 1]:
            mais_leve.clear()
            mais_leve.append(cadastro[valor + 0])
            mais_leve.append(cadastro[valor + 1])
        elif mais_leve[-1] == cadastro[valor + 1]:
            mais_leve.append(cadastro[valor + 0])
            mais_leve.append(cadastro[valor + 1])
        
print(f'A(s) pessoa(s) mais pesada(s) pesam {mais_pesada[-1]} kg e são', end='')
for valor in range(0, len(mais_pesada), 2):
    terminador = ','
    if valor == len(mais_pesada) - 2:
        terminador = '.\n'
    print(f' {mais_pesada[valor]}', end=terminador)

print(f'A(s) pessoa(s) mais leve(s) pesam {mais_leve[-1]} kg e são', end='')
for valor in range(0, len(mais_leve), 2):
    terminador = ','
    if valor == len(mais_leve) - 2:
        terminador = '.\n'
    print(f' {mais_leve[valor]}', end=terminador)
