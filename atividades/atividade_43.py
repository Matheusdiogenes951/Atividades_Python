# atvd 43
42

def pode_formar_triangulo(l1, l2, l3):
    """
    Verifica se três retas podem formar um triângulo.
    A soma de dois lados deve ser maior que o terceiro.
    """
    condicao1 = l1 + l2 > l3
    condicao2 = l1 + l3 > l2
    condicao3 = l2 + l3 > l1
    return condicao1 and condicao2 and condicao3

try:
    reta1 = float(input("Digite o comprimento da primeira reta: "))
    reta2 = float(input("Digite o comprimento da segunda reta: "))
    reta3 = float(input("Digite o comprimento da terceira reta: "))

    if reta1 <= 0 or reta2 <= 0 or reta3 <= 0:
        print("Os comprimentos das retas devem ser valores positivos.")
    elif pode_formar_triangulo(reta1, reta2, reta3):
        print("As três retas podem formar um triângulo!")

        if reta1 == reta2 and reta2 == reta3:
            print("É um triângulo equilátero.")
        elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
            print("É um triângulo isósceles.")
        else:
            print("É um triângulo escaleno.")

    else:
        print("As três retas NÃO podem formar um triângulo.")

except ValueError:
    print("Entrada inválida. Digite apenas números.")