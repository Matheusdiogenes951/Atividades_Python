dados = dict()

dados['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
gols = list()
for c in range(0, partidas):
    gols.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
dados['Gols'] = gols
dados['Total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O Campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas')

for i in range(0, partidas):
    print(f'   => Na partida {i + 1}, fez {dados["Gols"][i]} gols.')
print(f'Foi um total de {dados["Total"]} gols.')

