from Python3_Mundo3.atividades.Modulos.ex116c.lib.interface import *
from Python3_Mundo3.atividades.Modulos.ex116c.lib.arquivo import *
from Python3_Mundo3.atividades.atividade_114 import leiaInt

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu([' Ver Pessoas Cadastradas', ' Cadastrar  Pessoas', ' Sair'])
    if resposta == 1:
        #opcao de kistar um conteudo de arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #cadastra nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Digite o nome d: '))
        idade = leiaInt('Digite a idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabecalho('Saindo do sistema')
        break
    else:
        print('\033[31mERROR\033[m')
