'''
Crie um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
O nome de um jogador;
Quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def ficha(nome_jogador: str ='<desconhecido>', numero_gols: str ='0') -> str:
    return f'O jogador {nome_jogador} fez {numero_gols} gol(s) no campeonato.'


nome = input('Digite o nome do jogador: ').strip()
gols = input('Digite o número de gols: ')

if not gols.isnumeric():
    gols = '0'

if nome == '':
    print(ficha(numero_gols=gols))
else:
    print(ficha(nome, gols))
