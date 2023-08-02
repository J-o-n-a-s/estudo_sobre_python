'''
Crie um programa que leia vários numeros inteiro pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag de parada).
'''

numero = 0
contador = 0
somatoria = 0

while numero != 999:
    numero = int(input('Digite um número (999 para parar):'))
    if numero != 999:
        contador += 1
        somatoria += numero
print(f'\nForam digitados {contador} números e a soma é {somatoria}.')
