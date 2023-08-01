'''
Crie um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexos = ('M', 'F')
sexo = ''

while sexo not in sexos:
    sexo = input('Informe o seu sexo [M/F]: ').upper().strip()[0]
    if sexo not in sexos:
        print(f'Opção "{sexo}" inválida. Tente novamente.')

print(f'Seu sexo é "{sexo}", agradecemos por informar.\nAté mais!!!')
