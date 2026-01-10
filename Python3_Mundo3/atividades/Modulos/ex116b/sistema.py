from Python3_Mundo3.atividades.Modulos.ex116b.lib.interface import *
from Python3_Mundo3.atividades.Modulos.ex116b.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu([' Ver Pessoas Cadastradas', ' Cadastrar  Pessoas', ' Sair'])
    if resposta == 1:
        #opcao de kistar um conteudo de arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Opcao 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema')
        break
    else:
        print('\033[31mERROR\033[m')
