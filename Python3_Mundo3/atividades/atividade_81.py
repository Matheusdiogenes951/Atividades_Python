valores = []

while True:
    valor = int(input("Digite um valor: "))
    valores.append(valor)

    opcao = input("Quer continuar? [S/N] ").strip().upper()
    if opcao == 'N':
        break

print("-=" * 30)
print(f"Você digitou os valores {sorted(valores)}")
print("Programa encerrado.")         