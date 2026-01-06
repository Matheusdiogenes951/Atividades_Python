def ficha(jog="<desconhecido>", gol=0):
    print(f"O jogador {jog} fez {gol} gols no campeonato.")



# Programa Principal
while True:
    print("-" * 30)
    n = str(input("Nome do jogador: "))
    g = str(input("Numero de gols: "))
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if n.strip() == "":
        ficha(gol=g)
    else:
        ficha(n, g)

    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp in "N":
        break

