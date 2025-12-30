expressao = input("Digite uma expressão: ")
pilha = []

for char in expressao:
    if char == '(':
        pilha.append(char)
    elif char == ')':
        if not pilha:
            print("Sua expressão é inválida")
            break
        pilha.pop()
else:
    if not pilha:
        print("Sua expressão é válida")
    else:
        print("Sua expressão é inválida")


 