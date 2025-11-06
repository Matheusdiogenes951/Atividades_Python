# atvd 57
56

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):

    print("-----PESSOA {}-----".format(p))
    nome = str(input("NOME: ")).strip().capitalize()
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO [M/F]: ")).strip().upper()

    somaidade += idade


    if sexo == "M":
        if idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome

    if sexo == "F" and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4

print("A média de idade do grupo é de {:.2f} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))