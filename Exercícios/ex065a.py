'''
Crie um programa que leia vários números inteiros no teclado pelo teclado.
No final da excução, mostre a média entre todos os valores e qual foi o menor e o maior valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

numero = 0
contador = 0
somatoria = 0
primeiro = True
continuar = True

while continuar:
    numero = int(input('Digite um número:'))
    if primeiro:
        primeiro = False
        minimo = numero
        maximo = numero
    else:
        if minimo > numero:
            minimo = numero
        
        if maximo < numero:
            maximo = numero
            
    seguir = input('Deseja inserir mais números [S/N]? ').strip().upper()[0]
    
    if seguir == 'N':
        continuar = False
    elif seguir not in 'SN':
        print('Você digitou uma opção inválida, continuando...')
        
    contador += 1
    somatoria += numero
        
print(f'\nForam digitados {contador} números e a média é {(somatoria / contador):.2f}.')
print(f'O menor valor é {minimo}, o maior valor é {maximo} e a soma é {somatoria}.')
