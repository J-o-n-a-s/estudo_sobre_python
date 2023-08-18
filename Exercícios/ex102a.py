'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
O primeiro chamado numero que indique o valor para calcular;
O segundo chamado show que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
Obs.: Deverá ser implementado também a docstring na função para apresentar com a função help().
'''

def fatorial(numero: int, show: bool =False) -> str:
    '''
    -> Calcula o fatorial de um número inteiro
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não como é realizado o calculo fatorial.
    :return: O resultado do fatorial do número.
    '''
    
    valor = 1
    retorno = ''
    
    for contagem in range(numero, 0, -1):
        valor *= contagem
        if show:
            if contagem != 1:
                retorno += f'{contagem} x '
            else:
                retorno += f'{contagem} = {valor}\n'

    if not show:
        retorno = f'O fatorial do número {numero} é {valor}\n.'
        
    return retorno


print(fatorial(numero=5, show=True))
help(fatorial)
