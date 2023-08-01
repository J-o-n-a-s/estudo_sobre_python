'''
Crie um programa que leia um número qualquer e mostre o seu fatorial (usando "for" e usando "while").

Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120.
'''

print('-' * 35, '\nCÁLCULO FATORIAL DE UM NÚMERO\n')

numero = int(input('Digite um número: '))
copia_numero = numero
resultado = 1

print(f'{copia_numero}', end='')

while copia_numero > 1:
    resultado *= copia_numero
    copia_numero -= 1
    print(f' x {copia_numero}', end='')

print(f' = {resultado}')
print(f'\nO resultado de {numero}! é {resultado}.')
print('-' * 35)
