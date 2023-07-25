frase = input('Digite uma frase: ').strip()
print(f'A letra "A" aparece {frase.upper().count("A")} vezes.')
print(f'A letra "A" aparece a primeira vez na posição {frase.upper().find("A") + 1}.')
print(f'A letra "A" aparece a primeira vez na posição {frase.upper().rfind("A") + 1}.')