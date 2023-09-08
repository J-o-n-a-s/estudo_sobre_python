'''
Dentro do pacote utilidadesCeV que criamos no exercício 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que consiga funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que sejam monetários.
'''

from utilidadesCeV import dado, moeda

preco = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(preco, 80, 35)
