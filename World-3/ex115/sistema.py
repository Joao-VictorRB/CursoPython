from time import sleep
from lib import *
from arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    CriarArquivo(arq)

while True:
 resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa','Sair do Sistema'])
 if resposta == 1:
  #opção de listar conteúdo de um arquivo!
  LerArquivo(arq)
 elif resposta == 2:
  cabeçalho('NOVO CADASTRO')
  nome = input('Nome: ')
  idade = leiaInt('Idade: ')
  Cadastrar(arq, nome, idade)
 elif resposta == 3:
  cabeçalho('Saindo do sistema... até logo')
  break
 else:
  print('\033[mERRO! Digite uma opção válida!\033[m')
 sleep(2) 