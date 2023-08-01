'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. (DIGITAR SEM ACENTUAÇÃO)

Exemplos:
 - APOS A SOPA;
 - A SACADA DA CASA;
 - A TORRE DA DERROTA;
 - O LOBO AMA O BOLO;
 - ANOTARAM A DATA DA MARATONA.
'''

from time import sleep


frase = input('Digite uma frase sem acentuação: ')

print('\nAnalizando a frase...\n')
sleep(1.5)

frase_meio_sanitizada = frase.upper().strip()
frase_sanitizada = frase_meio_sanitizada.replace(' ', '')
frase_sanitizada_invertida = frase_sanitizada[::-1]

print(f'O inverso da frase {frase_sanitizada} é {frase_sanitizada_invertida}.')

if frase_sanitizada == frase_sanitizada_invertida:
    print(f'A frase "{frase_meio_sanitizada}" É UM PALÍNDROMO!')
else:
    print(f'A frase "{frase_meio_sanitizada}" NÃO É UM PALÍNDROMO!')
