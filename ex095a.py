'''
Aprimore o desafio 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.
'''

jogadores = []
jogador = {}

while True:
    total = 0
    jogador.clear()
    jogador['Nome'] = input('Digite o nome do jogador: ').strip()
    numero_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Gols'] = []
    
    for contador in range(0, numero_partidas):
        jogador['Gols'].append(int(input(f'Quantos gols {jogador["Nome"]} fez na partida {contador + 1}? ')))
        total += jogador['Gols'][contador]
        
    jogador['Total'] = total
    
    jogadores.append(jogador.copy())
    
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
        
        if continuar in 'SN':
            break
        
        print('ERRO! Por favor, digite só S ou N.')
    
    if continuar == 'N':
        break
    
print('-=' * 30 + '-')
print(f'{"Cód.":<5}' + f'{"Nome":<15}' + f'{"Gols":<15}' + 'Total')
print('-' * 40)

for numero, jogador in enumerate(jogadores):
    print(f'{numero:>4}' + f' {jogador["Nome"]:<15}' + f'{jogador["Gols"]}' + f'{jogador["Total"]:>3}')

print('-' * 40)

while True:
    mostrar = int(input('Os dados de qual jogador deseja mostrar? (999 para parar) '))
    
    if mostrar == 999:
        print('Até logo!')
        break
    
    print('Algo do jogador')
