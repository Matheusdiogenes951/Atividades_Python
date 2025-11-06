# atvd 60
59

n1 = int(input("Digite um valor: "))
n2 = int(input("digite outro valor: "))
opcao = 0

while opcao != 5:
    print("""   [1]somar
    [2]Multiplicar
    [3]Maior
    [4]Novos numeros
    [5]Sair""")



    opcao = int(input("qual a sua opcao? "))



    if opcao == 1:
        soma = n1 + n2
        print("a soma entre {} e {} e {}".format(n1, n2, soma))


    elif opcao == 2:
        multi = n1 * n2
        print("a multiplicacao entre {} e {} e {}".format(n1, n2, multi))


    elif opcao == 3:
        if n1 > n2:
            print("o maior e o {}".format(n1))
        elif n1 < n2:
            print("o maior e {}".format(n2))



    elif opcao == 4:
        print("informe os numeros novamente: ")
        n1 = int(input("Digite um valor: "))
        n2 = int(input("digite outro valor: "))



    elif opcao == 5:
        print("finalizando...")

    else:
        print("opcao invalida")



print("fim do programa!!! volte sempre")