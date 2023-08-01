'''
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

inicio = 1
fim = 11

tabuada = int(input('De qual número quer a tabuada? '))
for contagem in range(inicio, fim):
    print(f'{tabuada} x {contagem:2} = {tabuada * contagem}')