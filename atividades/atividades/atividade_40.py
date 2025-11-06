# atvd 40
39

idade = int(input('digite a sua idade: '))
alistamento = 18

if idade > alistamento:
    tempo = idade - alistamento
    print('já passou do prazo de alistamento')
    print('se passou {} anos do prazo'.format(tempo))
elif idade < alistamento:
    tempo = alistamento - idade
    print('ainda não chegou sua hora de se alistar')
    print('ainda faltam {} anos pra você se alistar'.format(tempo))
else:
    print('está na hora de você se alistar')