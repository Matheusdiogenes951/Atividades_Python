pessoas = []
while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

if pessoas:
    pesos = [p[1] for p in pessoas]
    max_peso = max(pesos)
    min_peso = min(pesos)
    pesadas = [p[0] for p in pessoas if p[1] == max_peso]
    leves = [p[0] for p in pessoas if p[1] == min_peso]
    print(f'O maior peso foi de {max_peso}Kg. Peso de {pesadas}')
    print(f'O menor peso foi de {min_peso}Kg. Peso de {leves}')
else:
    print('Nenhuma pessoa cadastrada.')
