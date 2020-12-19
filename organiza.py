import os

#0-Injeta o script na pasta
#1-criar pastas para armazenar arquivos específicos
#2-Pegar a extensão desses arquivos
#3- movê-los para a pasta adequada

def move_arquivo(arquivo,pasta):
    arquivo = os.path.relpath(arquivo)
    pasta = os.path.relpath(pasta)
    pasta = os.path.join(pasta,arquivo)
    os.rename(arquivo,pasta)
    print(f'moved {arquivo} -> {pasta}')
    
def pega_extensao(arquivo):
    #pega extensao do arquivo
    ponto = arquivo.rfind('.')
    extensao = arquivo[ponto:]
    return extensao

def organiza_arquivos():
    extensao_audio = ['.mp3','.wav','.wma','.ogg']
    extensao_documentos =['.doc','.docx','.xls','.pdf','.xlsx']
    extensao_video = ['.avi','.mov','.wmv','.mp4']
    extensao_imagens = ['.jpg','.png','.gif','.jpeg']
    
    lista = os.listdir('.')
    for arquivo in lista:
        if os.path.isfile(arquivo):
            extensao = pega_extensao(arquivo)
            if extensao in extensao_audio:
                move_arquivo(arquivo,'Audio')
            elif extensao in extensao_video:
                move_arquivo(arquivo,'Videos')
            elif extensao in extensao_documentos:
                move_arquivo(arquivo,'Documentos')
            elif extensao in extensao_imagens:
                move_arquivo(arquivo,'Imagens')
            else:
                move_arquivo(arquivo,'Outros')
        
def cria_pastas():
    lista_de_pastas = ['Imagens','Videos','Documentos','Outros','Audio']

    for pasta in lista_de_pastas:
        if not os.path.isdir(pasta):
            os.mkdir(pasta)
        else:
            print('A pasta ', pasta, ' já existe !!!')

    organiza_arquivos()
    
def injeta_script(diretorio):
    script_Organizador = os.path.abspath('organiza.py')
    os.chdir(diretorio)
    diretorio_Atual = os.path.abspath(diretorio)
    # faz uma cópia do script e manda para a pasta a ser organizada
    copiar = os.system('copy ' + script_Organizador + ' ' + diretorio_Atual) 
    cria_pastas()
    
directory = input('Digite o caminho do diretório que deseja organizar ex: C:\\Users\\Desktop ->')

injeta_script(directory)
