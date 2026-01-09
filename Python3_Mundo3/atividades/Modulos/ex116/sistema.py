from Python3_Mundo3.atividades.Modulos.ex116.lib.interface import *

while True:
    resposta = menu([' Ver Pessoas Cadastradas', ' Cadastrar  Pessoas', ' Sair'])
    if resposta == 1:
        cabecalho('Opcao 1')
    elif resposta == 2:
        cabecalho('Opcao 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema')
        break
    else:
        print('\033[31mERROR\033[m')
