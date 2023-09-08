'''
Modifique as funções que foram criadas no exercício 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda,
desenvolvido no exercício 108.
'''

from moeda import aumentar, diminuir, dobro, metade, moeda

preco = float(input('Digite o preço R$ '))
print(f'A metade do {moeda(preco)} é {metade(preco, True)}.')
print(f'O dobro do {moeda(preco)} é {dobro(preco, True)}.')
print(f'Aumentando 10%, temos {aumentar(preco,10, True)}.')
print(f'Diminuindo 13%, temos {diminuir(preco, 13, True)}.')
