dados = dict()
time = list()
partidas = list()
gols = list()

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    dados['gols'] = gols
    dados['Total'] = sum(gols)
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break


print('-=' * 30)
print('Cod ', end='')
for i in dados.keys():
    print(f'{k:<15}', end='')
print()

print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   => Na partida {i + 1}, fez {g} gols.')
    print('-=' * 30)
print('<< VOLTE SEMPRE >>')


