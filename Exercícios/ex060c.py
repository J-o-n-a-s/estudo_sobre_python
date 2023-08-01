'''
Crie um programa que leia um número qualquer e mostre o seu fatorial (usando "for" e usando "while").

Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120.
'''

print('-' * 35, '\nCÁLCULO FATORIAL DE UM NÚMERO\n')

numero = int(input('Digite um número: '))
resultado = numero

print(f'{numero}', end='')

for contador in range(numero - 1, 0, -1):
    resultado *= contador
    print(f' x {contador}', end='')

print(f' = {resultado}')
print(f'\nO resultado de {numero}! é {resultado}.')
print('-' * 35)
