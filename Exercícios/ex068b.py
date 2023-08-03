'''
Crie um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint

texto = 'VALOR JOGAR PAR OU ÍMPAR'
contador = 0

print('-=' * 20 + '-')
print(f'{texto:^41}')
print('-=' * 20 + '-')

while True:
    numero = int(input('Diga um valor: '))
    computador = randint(0, 10)
    selecao = ' '

    while selecao not in 'PI':
        selecao = input('Par ou Ímpar? [P/I] ').strip().upper()[0]

    soma = numero + computador
    par_impar = soma % 2
    print('-' * 41)
    print(f'Você jogou {numero} e o computador {computador}.\nO total deu {soma}, ', end='')
    
    print('DEU PAR!!!' if par_impar == 0 else 'DEU ÍMPAR!!!')
            
    if (par_impar == 0 and selecao == 'P') or (par_impar != 0 and selecao == 'I'):
        print('-' * 41)
        print('Você VENCEU!!!')
        print('Vamos Jogar novamente...')
        contador += 1
    else:
        print('-' * 41)
        print('Você PERDEU!!!')
        break
        
print(f'GAME OVER! Você venceu {contador} vezes.')
