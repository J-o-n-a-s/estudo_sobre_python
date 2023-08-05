'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numeros_extenso = (
    'zero',
    'um',
    'dois',
    'três',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'quatorze',
    'quinze',
    'dezesseis',
    'dezessete',
    'dezoito',
    'dezenove',
    'vinte'
)

while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <=20:
            break

    print(f'\nVocê digitou o número {numeros_extenso[numero]}.')

    while True:
        continuar = input('\nDeseja continuar? [S/N] ').strip().upper()[0]

        if continuar in 'SN':
            break

    if continuar == 'N':
        break

