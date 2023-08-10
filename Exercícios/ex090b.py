'''
Crie um programa que leia nome e média de um aluno guardando também a situação em um dicionário.
No final mostre o conteúdo da estrutura na tela.
'''

boletim = {}

boletim['Nome'] = input('Digite o nome do aluno: ')
boletim['Média'] = float(input(f'Digite a média do(a) aluno(a) {boletim["Nome"]}: '))

if boletim['Média'] >= 7:
    situacao = 'aprovado'
elif boletim['Média'] < 5:
    situacao = 'reprovado'
else:
    situacao = 'recuperação'

boletim['Situação'] = situacao

print('\n' + '-=' * 30 + '-')

for chave, valor in boletim.items():
    print(f'  - {chave} é igual a {valor}.')
