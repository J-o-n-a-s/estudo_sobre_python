'''
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Tranfira todas as funções utilizadas nos exercícios 107, 108, 109 e 110 para o primeiro pacote
e mantenha tudo funcionando.
'''

from utilidadesCeV import moeda

preco = float(input('Digite o preço R$ '))
moeda.resumo(preco, 80, 35)
