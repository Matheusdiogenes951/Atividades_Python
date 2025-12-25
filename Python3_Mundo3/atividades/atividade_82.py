valores = []
cont = 0

while True:
    valor = int(input("Digite um valor: "))
    valores.append(valor)

    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()
    if opcao == 'N':
         print("\nPrograma encerrado.")
         break

    for  valor in valores:
     cont +=1


print("-=" * 30)
if 5 in valores:
     print("O valor 5 faz parte da lista")
else:
     print("Vc n digitou o valor 5")

print("-=" * 30)
print(f"Voce digitou {(cont)-1} valores")
print(f"Voce digitou os valores {sorted(valores, reverse=True)}")
print("-=" * 30)        