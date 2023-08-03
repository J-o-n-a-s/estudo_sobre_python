'''
Crie um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    numero = int(input('Deseja ver a tabuada de qual valor? '))
    
    print('-' * 42)

    if numero < 0:
        break
    
    for contador in range(0, 11):
        print(f'{numero} x {contador:2} = {numero * contador}')
    
    print('-' * 42)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
