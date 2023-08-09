'''
Crie um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

- Quantas pessoas foram cadastradas;
- Uma listagem com as pessoas mais pesadas;
- Uma listagem com as pessoas mais leves.
'''

cadastro = []
maior_peso = 0
menor_peso = 0

while True:
    cadastro.append(input('Digite o nome: ').strip())
    cadastro.append(float(input('Digite o peso: kg ')))
    
    if len(cadastro) == 2:
        maior_peso = cadastro[-1]
        menor_peso = cadastro[-1]
    else:
        if maior_peso < cadastro[-1]:
            maior_peso = cadastro[-1]
            
        if menor_peso > cadastro[-1]:
            menor_peso = cadastro[-1]
    
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
    if cadastro[valor + 1] == maior_peso:
        mais_pesada.append(cadastro[valor + 0])
    
    if cadastro[valor + 1] == menor_peso:
        mais_leve.append(cadastro[valor + 0])

print(f'A(s) pessoa(s) mais pesada(s) pesam {maior_peso} kg e são', end='')
for numero, valor in enumerate(mais_pesada):
    terminador = ','
    if numero == len(mais_pesada) - 1:
        terminador = '.\n'
    print(f' {valor}', end=terminador)

print(f'A(s) pessoa(s) mais leve(s) pesam {menor_peso} kg e são', end='')
for numero, valor in enumerate(mais_leve):
    terminador = ','
    if numero == len(mais_leve) - 1:
        terminador = '.\n'
    print(f' {valor}', end=terminador)
