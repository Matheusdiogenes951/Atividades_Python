lista = []

v1 = int(input("Digite um valor: "))
lista.append(v1)
print("Valor adicionado com sucesso...  ")

v2 = int(input("Digite outro valor: "))
lista.insert(0, v2)
print("Valor adicionado com sucesso na pos 0 ")

v3 = int(input("Digite outro valor: "))
lista.insert(1, v3) 
print("Valor adicionado com sucesso na pos 1  ")

v4 = int(input("Digite outro valor: "))
lista.append(v4)
print("Valor adicionado com sucesso no final da lista ")

v5 = int(input("Digite outro valor: "))
lista.insert(0, v5)

print("Valor adicionado com sucesso na pos 0 ")

print("-=" * 30)
print(f"Os valores digitados foram: {lista}")
print("-=" * 30)
