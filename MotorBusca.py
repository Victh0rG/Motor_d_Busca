# encoding: utf-8

import os


nome_arquivo = "Lei_n°7998-1990"

"""def buscar_diretorio():
    #input nome_arquivo = Lei_n°tal

    tipo_dir = nome_arquivo[0:3]
    dicionario= {"Lei": 1,
                 "Dec": 2,
                 "Por": 3,
                 "Out": 4}


    if tipo_dir == "Lei":
        #diretorio =
        #dicionario = {tipo_dir: diretorio}
    print("Hello")"""

# Definir o diretório pai
diretorio_pai = "Arquivos/"

def explorar_diretorios(diretorio):
    # Listar todos os itens no diretório

    for diretorio in os.listdir(diretorio):
        caminho_item = os.path.basename(diretorio)

        # Verificar se é um diretório
        if os.path.isdir(caminho_item):
            print(f"Diretório encontrado: {caminho_item}")
            # Chamada recursiva para explorar subdiretórios
            explorar_diretorios(caminho_item)
        else:
            print(f"Arquivo encontrado: {caminho_item}")


# Iniciar a exploração
explorar_diretorios(diretorio_pai)



def buscar_arquivos(pasta_raiz, extensao=".pdf"):

    try:
        arquivos_encontrados = {}

        for pasta_atual, subpastas, arquivos in os.walk(pasta_raiz):
            for arquivo in arquivos:
                if arquivo.endswith(extensao):

                    caminho_completo = os.path.join(pasta_raiz, arquivo)
                    arquivos_encontrados[arquivo] = caminho_completo

                    return arquivos_encontrados[arquivo]

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {FileNotFoundError} ")


resultado = buscar_arquivos("Arquivos/Leis/")



print(resultado)

