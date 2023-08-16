'''
Crie um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função citada:

De 1 até 10, de 1 em 1;
De 10 até 0, de 2 em 2;
Uma contagem personalizada.
'''

from time import sleep

def contador(inicio: int, fim: int, passo: int):
    if inicio > fim and passo > 0:
        passo_interno = passo * (-1)
    elif inicio > fim and passo < 0:
        passo_interno = passo
        passo *= -1
    elif passo == 0:
        if inicio > fim:
            passo_interno = -1
        else:
            passo_interno = 1
    else:
        passo_interno = passo
    
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    for contagem in range(inicio, fim + passo_interno, passo_interno):
        if (inicio > fim and contagem >= fim) or (inicio < fim and contagem <= fim):
            sleep(0.75)
            print(f'-> {contagem} ', end='', flush=True)
    
    print('\n' + '-=' * 40 + '-')


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio_personalizado = int(input('Início: '))
fim_personalizado = int(input('Fim: '))
passo_personalizado = int(input('Passo: '))
contador(inicio_personalizado, fim_personalizado, passo_personalizado)
