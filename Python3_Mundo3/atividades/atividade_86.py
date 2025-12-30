valor = []
princ = [[], []]
for c in range (0,8):
    valor.append(int(input('Digite um valor: ')))
    if valor % 2 == 0:
        princ[0].append(valor)
    else:
        princ[1].append(valor)



print('-=' * 30)
print(f'A lista de pares e {sorted(princ[0])}')
print(f'A lista de impares e {sorted(princ[1])}')