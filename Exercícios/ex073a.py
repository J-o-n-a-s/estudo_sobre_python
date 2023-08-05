'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:

Apenas os 5 primeiros colocados da tabela;
Os últimos 4 colocados da tabela;
Uma lista com os times em ordem alfabética;
Em que posição na tabela está o time da Tricolor Paulista (São Paulo Futebol Clube).
'''

times = (
    'Botafogo',
    'Flamengo',
    'Palmeiras',
    'Grêmio',
    'Fluminense',
    'Bragantino',
    'Athletico-PR',
    'São Paulo',
    'Cuiabá',
    'Cruzeiro',
    'Fortaleza',
    'Internacional',
    'Atlético-MG',
    'Corinthians',
    'Santos',
    'Goiás',
    'Bahia',
    'Coritiba',
    'América-MG',
    'Vasco da Gama'
)

print('-=' * 50 + '-')
print(f'Lista de tímes do Brasileirão: {times}.')
print('-=' * 50 + '-')
print(f'Os 5 primeiros colocados são: {times[:5]}.')
print('-=' * 50 + '-')
print(f'Os 4 últimos colocados são: {times[-4:]}.')
print('-=' * 50 + '-')
print(f'Os times em ordem alfabética são {sorted(times)}.')
print('-=' * 50 + '-')
print(f'O São Paulo está na {times.index("São Paulo") + 1}ª posição.')
print('-=' * 50 + '-')
