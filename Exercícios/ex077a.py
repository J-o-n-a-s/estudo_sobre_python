'''
Crie um programa que tenha uma tupla com várias palavras (Não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as sua vogais.
'''

palavras = (
    'APRENDER',
    'PROGRAMAR',
    'LINGUAGEM',
    'PYTHON',
    'CURSO',
    'GRATIS',
    'ESTUDAR',
    'PRATICAR',
    'TRABALHAR',
    'MERCADO',
    'PROGRAMADOR',
    'FUTURO'
)

for palavra in palavras:
    contador = 0
    numero_vogais = 0
    vogais = 'AEIOU'
    for letra in palavra:
        if letra in vogais:
            numero_vogais += 1
    print(f'Na palavra {palavra} temos {numero_vogais} vogais: ', end='')
    for letra in palavra:
        if letra in vogais:
            contador += 1
            if contador == numero_vogais:
                separador = '.\n'
            else:
                separador = ', '
            print(f'{letra}', end=separador)
