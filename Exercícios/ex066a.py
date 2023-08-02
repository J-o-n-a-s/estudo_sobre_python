'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

contador = 0
somatoria = 0

while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    contador += 1
    somatoria += numero

print(f'\nA soma dos {contador} valores foi {somatoria} e média é {(somatoria / contador):.2f}')
