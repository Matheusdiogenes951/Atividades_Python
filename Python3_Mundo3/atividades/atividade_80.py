valores = []

while True:
    valor = int(input("Digite um valor: "))
    if valor in valores:
        print("Valor duplicado! Não vou adicionar.")
    else:
        valores.append(valor)

    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()
    if opcao == 'N':
         print("\nPrograma encerrado.")
         break


    print("-=" * 30)
    print(f"Voce digitou os valores {sorted(valores)}")         