Valores = []
maior = 0
menor = 0
for c in range(0, 5):
    Valores.append(int(input(f"Digite um valor para a posicao {c}")))
    if c == 0:
        maior = menor = Valores[c]
    else:
        if Valores[c] > maior:
            maior = Valores[c]
        if Valores[c] < menor:
            menor = Valores[c]


print("-=" * 30)
print(f"Voce digitou os valores {Valores}")
print(f"O maior valor digitado foi {maior} nas posicoes ", end="")
for i, v in enumerate(Valores):
    if v == maior:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi {menor} nas posicoes ", end="")
for i, v in enumerate(Valores):
    if v == menor:
        print(f"{i}...", end="")
print()