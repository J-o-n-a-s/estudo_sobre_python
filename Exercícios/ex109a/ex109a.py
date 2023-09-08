'''
Adapte o código do desafio 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado.
'''

from moeda import aumentar, diminuir, dobro, metade, moeda

preco = float(input('Digite o preço R$ '))
print(f'A metade do {moeda(preco)} é {metade(preco, True)}.')
print(f'O dobro do {moeda(preco)} é {dobro(preco, True)}.')
print(f'Aumentando 10%, temos {aumentar(preco,10, True)}.')
print(f'Diminuindo 13%, temos {diminuir(preco, 13, True)}.')
