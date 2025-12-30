valores = []
Par = []
Impar = []
cont = 0

while True:
    valor = int(input("Digite um valor: "))
    valores.append(valor)


    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()
    if opcao == 'N':
         print("\nPrograma encerrado.")
         break

for valor in valores:
    if valor % 2 == 0:
        Par.append(valor)
    else:
        Impar.append(valor)

print("-=" * 30)

print("-=" * 30)
print(f"Voce digitou os valores {sorted(valores)}")
print(f"Os valores pares digitados foram {sorted(Par)}")
print(f"Os valores impares digitados foram {sorted(Impar)}")
print("-=" * 30)        