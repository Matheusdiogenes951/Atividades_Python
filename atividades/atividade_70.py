# atvd 70
69

pessoas_de_maior = 0
totmulher20 = 0
s = 'sair'
hc = 0


while True:
    nome = str(input("NOME: ")).strip().capitalize()
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO [M/F]: ")).strip().upper()


    if sexo == "M":
       hc += 1

    if sexo == "F" and idade < 20:
        totmulher20 += 1

    if idade >= 18:
        pessoas_de_maior += 1


    opcao = str(input("vc quer continuar?[S/N] ")).strip().upper()
    if opcao == 'N':
        print("programa encerrado")
        break


print(f"Tem {pessoas_de_maior} pessoas com idade igual ou superior a 18 anos")
print(f"Foram cadastrado {hc} homens")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos")