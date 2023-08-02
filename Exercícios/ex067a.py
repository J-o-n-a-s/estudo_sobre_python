'''
Crie um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    numero = int(input('Deseja ver a tabuada de qual valor? '))
    contador = 0
    
    if numero < 0:
        break
    
    print('-' * 42)
    
    while True:
        print(f'{numero} x {contador:2} = {numero * contador}')
        contador += 1
        if contador == 11:
            break
    
    print('-' * 42)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
