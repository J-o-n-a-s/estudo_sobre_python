'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.

Observação:

Uma lista compostas que conterá todas as informações dos alunos;
Dentro da lista principal conterá uma lista que contém o nome do aluno e uma lista com as duas notas. Exemplo:
[['Aluno1', [nota1, nota2], média], ['Aluno2', [nota1, nota2], média], ['Aluno3', [nota1, nota2], média]]
'''

informacoes_alunos = []
notas = []
numero_notas = 2

while True:
    nome = input('Digite o nome do aluno: ').strip()
    soma = 0
    media = 0
    
    for contador in range(0, numero_notas):
        notas.append(float(input(f'Digite a {contador + 1}ª nota: ')))
        soma += notas[contador]
    
    media = soma / numero_notas
    informacoes_alunos.append([nome, notas[:], media])
    notas.clear()
        
    continuar = ' '
    
    while continuar not in 'SN':
        continuar = input('Deseja continuar: [S/N] ').strip().upper()[0]
    
    if continuar == 'N':
        break

print('\n' + '-=' * 30 + '-')
print(f'{"Nº":<4}{"NOME":<20}{"MÉDIA":7}')
print('-' * 30)

for contador in range(0, len(informacoes_alunos)):
    print(f'{contador:<4}{informacoes_alunos[contador][0]:<20}{informacoes_alunos[contador][2]:>5.1f}')

print('-=' * 30 + '-')

while True:
    visualizar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if visualizar == 999:
        break
    
    if visualizar < len(informacoes_alunos):
        print(f'As notas de {informacoes_alunos[visualizar][0]} foram {informacoes_alunos[visualizar][1]}.\n')
