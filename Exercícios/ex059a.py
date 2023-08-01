'''
Crie um programa que leia 2 valores e mostre um menu na tela:

[1] Somar;
[2] Multiplicar;
[3] Maior;
[4] Novos números;
[5] Sair do programa.
Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep


opcao = 0
tempo = 2.5

print('-' * 33)
print('MENU')
numero_01 = float(input('Escolha o 1º número: '))
numero_02 = float(input('Escolha o 2º número: '))
while opcao != 5:
    print('\n', '-' * 5, 'Escolha uma das opção', '-' * 5)
    opcao = int(input('[1] Somar;\n[2] Multiplicar;\n[3] Maior;\n[4] Novos números;\n[5] Sair do programa.\n'))
    if opcao == 1:
        print(f'\nA soma entre os números {numero_01} e {numero_02} é {(numero_01 + numero_02)}.')
    elif opcao == 2:
        print(f'\nA multiplicação entre os números {numero_01} e {numero_02} é {(numero_01 * numero_02)}.')
    elif opcao == 3:
        if numero_01 > numero_02:
            resultado = f'\nO maior número entre {numero_01} e {numero_02} é {numero_01}.'
        elif numero_02 > numero_01:
            resultado = f'\nO maior número entre {numero_01} e {numero_02} é {numero_02}.'
        else:
            resultado = f'\nOs números {numero_01} e {numero_02} são iguais.'
        print(resultado)
    elif opcao == 4:
        numero_01 = float(input('\nEscolha o 1º número: '))
        numero_02 = float(input('Escolha o 2º número: '))
    elif opcao == 5:
        pass
    else:
        print(f'\nOpção {opcao} inválida. Tente novamente.')
    sleep(tempo)
print('\nObrigado e até mais!!!')        
