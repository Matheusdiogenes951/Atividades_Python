def area(larg, comp):
    a = larg * comp
    print(f"A areao de um terreno {larg}X{comp} e de {a}m²")


print("Controle de Terrenos")
print("-" * 25)
l = float(input("Largura: "))
c = float(input("Comprimento:"))
area(l, c)