import random
aluno01 = input('Primeiro aluno: ')
aluno02 = input('Segundo aluno: ')
aluno03 = input('Terceiro aluno: ')
aluno04 = input('Quarto aluno: ')
alunos = [aluno01, aluno02, aluno03, aluno04]
random.shuffle(alunos)
print(f'O aluno escolhido foi {alunos}.')