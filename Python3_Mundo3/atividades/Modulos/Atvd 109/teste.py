import Moeda

p = float(input('Digite um preco: '))
print(f'A metade de {Moeda.moeda(p)} e {Moeda.moeda(Moeda.metade(p))}')
print(f'O dobro de {Moeda.moeda(p)} e {Moeda.moeda(Moeda.dobro(p))}')
print(f'Aumentando 10 %, temos {Moeda.moeda(Moeda.aumentar(p, 10))}')
print(f'Diminuindo 10 %, temos {Moeda.moeda(Moeda.diminuir(p, 10))}')

