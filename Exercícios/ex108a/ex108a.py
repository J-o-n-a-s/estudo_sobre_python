'''
Adapte o código do exercício 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado.
'''

from moeda import aumentar, diminuir, dobro, metade, moeda

preco = float(input('Digite o preço R$ '))
print(f'A metade do {moeda(preco)} é {moeda(metade(preco))}.')
print(f'O dobro do {moeda(preco)} é {moeda(dobro(preco))}.')
print(f'Aumentando 10%, temos {moeda(aumentar(preco,10))}.')
print(f'Diminuindo 13%, temos {moeda(diminuir(preco, 13))}.')
