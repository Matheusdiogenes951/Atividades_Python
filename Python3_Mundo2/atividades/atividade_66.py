# atvd 66
65

resp = 'S'
n = nd = media = cont = maior = menor = soma = meio = 0

while resp in 'Ss':
    n = int(input("Digite um número: "))
    soma += n
    nd += 1

    if nd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior  = n
        elif n < menor:
            menor = n


    resp = str(input("vc quer continuar? [S/N] ")).strip().upper()[0]
media = soma / nd
print("o maior numero digitado foi {}".format(maior))
print("o menor numero digitado foi {}".format(menor))
print("fim, vc digitou {} numeros e a media deles e {} ".format(nd, media))