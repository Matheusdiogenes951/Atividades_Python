# atvd 51
50

soma = 0
cont = 0
for i in range(1,7):
    numero = int(input("digite o valor {} ".format(c)))
    if numero % 2 == 0:
        soma = soma + numero
        cont = cont +1
print("vc informou {} numeros pares e a soma foi {}".format(cont, soma))