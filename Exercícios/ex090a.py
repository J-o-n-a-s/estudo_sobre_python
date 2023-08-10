'''
Crie um programa que leia nome e média de um aluno guardando também a situação em um dicionário.
No final mostre o conteúdo da estrutura na tela.
'''

boletim = {}

nome = input('Digite o nome do aluno: ').strip()
media = float(input(f'Digite a média do(a) aluno(a) {nome}: '))

if media >= 7:
    situacao = 'aprovado'
elif media < 5:
    situacao = 'reprovado'
else:
    situacao = 'recuperação'

boletim['Nome'] = nome
boletim['Média'] = media
boletim['Situação'] = situacao

print('\n' + '-=' * 30 + '-')

for chave, valor in boletim.items():
    print(f'  - {chave} é igual a {valor}.')
