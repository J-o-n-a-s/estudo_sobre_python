'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

from moeda import aumentar, diminuir, dobro, metade

preco = float(input('Digite o preço R$ '))
print(f'A metade do {preco} é {metade(preco)}.')
print(f'O dobro do {preco} é {dobro(preco)}.')
print(f'Aumentando 10%, temos {aumentar(preco,10)}.')
print(f'Diminuindo 13%, temos {diminuir(preco, 13)}.')
