'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input('Digite um número: ')))

    continuar = ' '
    
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    
    if continuar == 'N':
        break

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('-=' * 30 + '-')
print(f'A lista completa é {numeros}.')

if len(pares) > 0:
    print(f'A lista de pares é {pares}.')

if len(impares) > 0:
    print(f'A lista de ímpares é {impares}.')
