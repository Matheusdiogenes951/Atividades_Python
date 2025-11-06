# atvd 46
45

# Exemplo de código em Python
import random

# Opções de jogada
itens = ['pedra', 'papel', 'tesoura']

# Gere a jogada do computador
computador = random.choice(itens)

# Peça a jogada do jogador
print('Escolha entre Pedra, Papel ou Tesoura:')
jogador = input().lower() # Converte para minúsculas para facilitar a comparação

# Verifique se a jogada do jogador é válida
if jogador not in itens:
    print('Jogada inválida!')
else:
    print(f'Você jogou: {jogador}')
    print(f'O computador jogou: {computador}')

    # Lógica para determinar o vencedor
    if jogador == computador:
        print('Empate!')
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'tesoura' and computador == 'papel') or \
         (jogador == 'papel' and computador == 'pedra'):
        print('Você venceu!')
    else:
        print('O computador venceu!')