# atvd 69
68

import random

vitorias_consecutivas = 0
vitoria = True

while vitoria:
    escolha_jogador = input("Escolha par ou ímpar: ").lower().strip()
    numero_jogador = int(input("Digite um número: "))
    numero_computador = random.randint(0, 10)

    soma = numero_jogador + numero_computador
    if soma % 2 == 0:
        resultado = "par"
    else:
        resultado = "ímpar"

    if escolha_jogador == resultado:
        print(f"Você venceu! O computador escolheu {numero_computador}. A soma é {soma} ({resultado}).")
        vitorias_consecutivas += 1
    else:
        break

print(f"Fim do jogo. Você conquistou um total de {vitorias_consecutivas} vitórias consecutivas.")