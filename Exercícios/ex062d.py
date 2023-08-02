'''
Melhore o exercício 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''

contador = 1
primeiro_termo = int(input('Digite o primeiro termo para realizar uma progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
termo = primeiro_termo
numero_termos = 10
repete = False

print(primeiro_termo, end='')
while contador < numero_termos:
    termo += razao
    if repete == True:
        repete = False
        print(f'{termo}', end='')
    else:
        print(f' -> {termo}', end='')
    contador += 1
    if contador == numero_termos:
        mais_termos = int(input('\n\nVocê deseja mostrar mais termos, quantos? '))
        if mais_termos != 0:
            numero_termos += mais_termos
            repete = True
