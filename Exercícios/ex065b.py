'''
Crie um programa que leia vários números inteiros no teclado pelo teclado.
No final da excução, mostre a média entre todos os valores e qual foi o menor e o maior valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

numero = 0
contador = 0
somatoria = 0
seguir = 'S'

while seguir == 'S':
    numero = int(input('Digite um número:'))         
    seguir = input('Deseja inserir mais números [S/N]? ').strip().upper()[0]
    
    if seguir not in 'SN':
        seguir = 'S'
        print('Você digitou uma opção inválida, continuando...\n')
        
    contador += 1
    somatoria += numero

    if contador == 1:
        minimo = numero
        maximo = numero
    else:
        if minimo > numero:
            minimo = numero
        
        if maximo < numero:
            maximo = numero
        
print(f'\nForam digitados {contador} números e a média é {(somatoria / contador):.2f}.')
print(f'O menor valor é {minimo}, o maior valor é {maximo} e a soma é {somatoria}.')
