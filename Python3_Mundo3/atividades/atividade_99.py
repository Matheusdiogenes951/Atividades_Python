from time import sleep

def contador(i, f, p):
    print("-=" * 20)
    print(f"Contagem de {i} até {f} de {p} em {p}")
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end='')
            sleep(0.3)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end='')
            sleep(0.3)
            cont -= p
        print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input("Fim: "))
pas = int(input("Passo: "))
if pas <= 0:
    pas = 1
contador(ini, fim, pas)
