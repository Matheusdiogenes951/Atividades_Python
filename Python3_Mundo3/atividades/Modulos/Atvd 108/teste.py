import Moeda

p = float(input('Digite um preco: '))
print(f'A metade de {p} e {Moeda.metade(p)}')
print(f'O dobro de {p} e {Moeda.dobro(p)}')
print(f'Aumentando 10 %, temos {Moeda.aumentar(p, 10)}')
print(f'Diminuindo 10 %, temos {Moeda.diminuir(p, 10)}')

