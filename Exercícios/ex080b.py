'''
Crie um programa onde o usuário possa digitar cinco valores numéricos.
Cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
'''

numeros = []

for valor in range(0, 5):
    numero_digitado = int(input('Digite um número: '))
    if numero_digitado not in numeros:
        if valor == 0 or numero_digitado > numeros[-1]:
            numeros.append(numero_digitado)
            print('Adicionado ao final da lista...')
        else:
            for posicao in range(0, len(numeros)):
                if numero_digitado < numeros[posicao]:
                    numeros.insert(posicao, numero_digitado)
                    print(f'Adicionado na posição {posicao} da lista...')
                    break

print('-=' * 30 + '-')
print(f'Os números digitados foram: {numeros}.')
