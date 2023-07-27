'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

Média abaixo de 5.0 = REPROVADO;
Média entre 5.0 e 6.9 = RECUPERAÇÃO;
Média 7.0 ou superior = APROVADO.
'''

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = ((nota1 + nota2) / 2)
print(f'A média entre os valores {nota1:.1f} e {nota2:.1f} é {media:.1f}.\n')

if media < 5.0:
    print('Infelizmente, você foi REPROVADO!')
elif media >= 5.0 and media < 7.0:
    print('Você precisará estudar mais, você está de RECUPERAÇÃO!')
elif media >= 7.0:
    print('Parabéns! Você foi APROVADO!')