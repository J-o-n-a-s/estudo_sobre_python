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
    nome = input('Digite o nome: ').strip()
    peso = float(input('Digite o peso: kg '))
    cadastro.append([nome, peso])
    
    if len(cadastro) == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if maior_peso < peso:
            maior_peso = peso
            
        if menor_peso > peso:
            menor_peso = peso
    
    continuar = ' '
    
    while continuar not in 'SN':
        continuar = input('Deseja continuar com o cadastro? [S/N] ').strip().upper()[0]
    
    if continuar == 'N':
        break

print('\n' + '-=' * 30 + '-')
print(f'Os dados cadastrados foram {cadastro}.')
print(f'Foram cadastradas {len(cadastro)} pessoas.')
print(f'A(s) pessoa(s) mais pesada(s) pesam {maior_peso} kg e são', end='')

for pessoa in cadastro:
    if pessoa[1] == maior_peso:
        print(f' -> {pessoa[0]}', end='')

print(f'.\nA(s) pessoa(s) mais leve(s) pesam {menor_peso} kg e são', end='')

for pessoa in cadastro:
    if pessoa[1] == menor_peso:
        print(f' -> {pessoa[0]}', end='')
        
print('.\n')
