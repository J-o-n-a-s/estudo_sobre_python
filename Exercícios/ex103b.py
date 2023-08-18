'''
Crie um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
O nome de um jogador;
Quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def ficha(nome_jogador: str ='', numero_gols: str ='0') -> str:
    if nome_jogador == '':
        nome_jogador = '<desconhecido>'
    
    if not numero_gols.isnumeric():
        numero_gols = '0'
        
    return f'O jogador {nome_jogador} fez {numero_gols} gol(s) no campeonato.'
    
    
print(
    ficha(
        input('Digite o nome do jogador: ').strip(),
        input('Digite o número de gols: ')
    )
)
