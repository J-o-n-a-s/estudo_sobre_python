'''
Crie um programa que leia o peso e altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:

Abaixo de 18.5: Abaixo do peso;
Entre 18.5 e 25: Peso ideial;
Entre 25 e 30: Sobrepeso;
Entre 30 e 40: Obesidade;
Acima de 40: Obesidade mórbida.
'''

from time import sleep


peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)
print(f'O seu peso é {peso:.1f} kg e a sua altura é {altura:.2f} m.\nAnalisando...')
sleep(3)

if imc < 18.5:
    print(f'Você está abaixo do seu peso ideal. Seu IMC deu {imc:.1f}.')
elif imc >= 18.5 and imc < 25:
    print(f'Você está no seu peso ideal. Seu IMC deu {imc:.1f}.')
elif imc >= 25 and imc < 30:
    print(f'Você está com sobrepeso. Seu IMC deu {imc:.1f}.')
elif imc >= 30 and imc < 40:
    print(f'Você está com obesidade. Seu IMC deu {imc:.1f}.')
elif imc >= 40:
    print(f'Você está com obesidade mórbida. Seu IMC deu {imc:.1f}.')