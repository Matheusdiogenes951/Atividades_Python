# atvd 65
64

n = nd = soma = cont = 0
n = int(input("Digite um número: "))
while n != 999:
    cont += 1
    soma += n
    nd += 1
    n = int(input("Digite um número: "))
print("fim, vc digitou {} numeros e a soma deles e {} ".format(nd, soma))