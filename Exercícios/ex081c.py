'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

Quantos números foram digitados;
A lista de valores ordenada de forma decrescente;
Se o valor 5 foi digitado e está ou não na lista.
'''

numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))

    continuar = ' '
    
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    
    if continuar == 'N':
        break

print('-=' * 30 + '-')
print(f'Você digitou {len(numeros)} números.')

numeros.sort(reverse=True)

print(f'Os valores em ordem decrescente são {numeros}.')

texto = 'faz parte' if 5 in numeros else 'não faz parte'

print(f'O valor 5 {texto} da lista!')
