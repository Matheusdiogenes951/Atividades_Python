# Programa para criar uma matriz 3x3 e preenchê-la com valores do teclado

# Declarar a matriz como uma lista de listas
matriz = []

# Preencher a matriz com valores lidos do teclado
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Mostrar a matriz na tela com formatação correta
print("\nMatriz 3x3:")
for linha in matriz:
    print(' '.join(map(str, linha)))
