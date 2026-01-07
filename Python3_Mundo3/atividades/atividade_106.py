def notas(a=0, b=0, c=0, sit=False):
    notas = [a, b, c]
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    if sit:
        if media >= 7:
            situacao = "BOA"
        elif media >= 5:
            situacao = "RAZOÁVEL"
        else:
            situacao = "RUIM"
        return maior, menor, media, situacao


# Programa principal
resp = notas(7.5, 8.0, 6.5, sit=True)
print(resp)