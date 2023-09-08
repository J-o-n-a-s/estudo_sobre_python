'''
Adicione ao módulo moeda.py criado nos exercícios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
'''

from moeda import aumentar, diminuir, dobro, metade, moeda, resumo

preco = float(input('Digite o preço R$ '))
resumo(preco, 80, 35)
