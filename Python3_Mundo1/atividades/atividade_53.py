# atvd 53
52

n = int(input('Digite um número: '))
total_divisores = 0

for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[34m{c}', end=' ')
        total_divisores += 1
    else:
        print(f'\033[31m{c}', end=' ')

print(f'\n\n\033[mO número {n} foi divisível {total_divisores} vezes.')
if total_divisores == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')