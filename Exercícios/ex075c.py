'''
Crie um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:

Quantas vezes apareceu o valor 9;
Em que posição foi digitado o primeiro valor 3;
Quais foram os números pares.
'''

contador_01 = 0
contador_02 = 0

numeros = (
    int(input('Digite o primeiro número: ')),
    int(input('Digite o segundo número: ')),
    int(input('Digite o terceiro número: ')),
    int(input('Digite o terceiro número: '))
)

print(f'\nVocê digitou os números {numeros}.')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 not in numeros:
    print(f'Não foi digitado o número 3.')
else:
    print(f'O número 3 foi digitado a primeria vez na posição {numeros.index(3) + 1}.')

for numero in numeros:
    if numero % 2 == 0:
        contador_01 += 1

if contador_01 == 0:
    print('Não foram digitados números pares.')
elif contador_01 == 1:
    for numero in numeros:
        if numero % 2 == 0:
            print(f'O único número par digitado foi {numero}.')
else:
    print('Os números pares digitados foram ', end='')
    for numero in numeros:
        if numero % 2 == 0:
            contador_02 += 1
            if contador_01 == contador_02:
                separador = '.'
            else:
                separador = ', '
            print(numero, end=separador)
