frase = input('Digite uma frase: ').upper().strip()
print(f'A letra "A" aparece {frase.count("A")} vezes.')
print(f'A letra "A" aparece a primeira vez na posição {frase.find("A") + 1}.')
print(f'A letra "A" aparece a primeira vez na posição {frase.rfind("A") + 1}.')