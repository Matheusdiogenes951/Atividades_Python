# atvd 49
48

soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print("a soma dos {} e igual a {}".format(cont, soma))