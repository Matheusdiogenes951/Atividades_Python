times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense  ',
         'Atlético-MG', 'Botafogo', 'Bahia', 'São Paulo',
         'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba',
         'Avaí', 'Ponte Preta', 'Atlético-PR', 'Ceará SC', 'Atlético-GO')

print("-=" * 20)
print(f"Lista de times: {times}")
print("-=" * 20)

print(f"Os 5 primeiros sao: {times[0:5]}")
print("-=" * 20)
print(f"Os 4 ultimos sao: {times[-4:]}")
print("-=" * 20)
print(f"Times em ordem alfabetica sao: {sorted(times)}")
print("-=" * 20)
print(f"O Ceara SC esta na {times.index("Ceará SC")+1} posicao")