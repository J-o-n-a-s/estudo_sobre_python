'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

aproveitamento = {}
total = 0

aproveitamento['Jogador'] = input('Digite o nome do jogador: ').strip()
numero_partidas = int(input(f'Quantas partidas {aproveitamento["Jogador"]} jogou? '))
aproveitamento['Gols'] = []

for contador in range(0, numero_partidas):
    aproveitamento['Gols'].append(int(input(f'Quantos gols {aproveitamento["Jogador"]} fez na partida {contador + 1}? ')))
    total += aproveitamento['Gols'][contador]
    
aproveitamento['Total'] = total

print('-=' * 30 + '-')
print(aproveitamento)
print('-=' * 30 + '-')

for chave, valor in aproveitamento.items():
    print(f'O campo "{chave}" tem o valor {valor}.')

print('-=' * 30 + '-')

print(f'O jogador {aproveitamento["Jogador"]} jogou {len(aproveitamento["Gols"])} partidas.')

for contador in range(0, len(aproveitamento["Gols"])):
    print(f'  => Na partida {contador + 1}, fez {aproveitamento["Gols"][contador]} gol(s).')
    
print(f'Foi um total de {aproveitamento["Total"]} gol(s).')
