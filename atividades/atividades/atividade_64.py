# atvd 64
63

n = int(input('Quantos elementos você quer ver na sequência de Fibonacci? '))

termo1 = 0
termo2 = 1
contador = 0

if n <= 0:
    print("Por favor, insira um número inteiro positivo.")
elif n == 1:
    print("Sequência de Fibonacci:")
    print(termo1)
else:
    print("Sequência de Fibonacci:")

    print(termo1, end=" ")
    print(termo2, end=" ")

    while contador < n - 2:
        proximo_termo = termo1 + termo2
        print(proximo_termo, end=" ")
        termo1 = termo2
        termo2 = proximo_termo
        contador += 1