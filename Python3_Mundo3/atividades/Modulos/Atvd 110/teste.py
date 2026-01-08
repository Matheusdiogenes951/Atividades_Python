import Moeda

p = float(input('Digite um preco: '))
print(f'A metade de {Moeda.moeda(p)} e {Moeda.metade(p, True):.2f}')
print(f'O dobro de {Moeda.moeda(p)} e {Moeda.dobro(p, True)}')
print(f'Aumentando 10 %, temos {Moeda.aumentar(p, 10)}')
print(f'Diminuindo 10 %, temos {Moeda.diminuir(p, 10, True)}')

