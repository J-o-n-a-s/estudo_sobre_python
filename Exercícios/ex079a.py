'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número ja exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

numeros = []

while True:
    numero = int(input('Digite um número: '))

    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não será adicionado...')

    resposta = ' '

    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if resposta == 'N':
        break

numeros.sort()

print('-=' * 30 + '-')
print(f'Os números digitados são {numeros}.')
