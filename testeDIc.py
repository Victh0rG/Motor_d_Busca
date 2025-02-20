import os


def buscar_pdfs(diretorios):
    resultado = {}

    for diretorio in diretorios:
        # Verifica se o diretório existe
        if os.path.exists(diretorio) and os.path.isdir(diretorio):
            # Lista arquivos .pdf no diretório
            arquivos_pdf = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.pdf')]
            resultado[diretorio] = arquivos_pdf
        else:
            resultado[diretorio] = f"Diretório {diretorio} não encontrado ou não é válido."

    return resultado


# Lista de diretórios a serem buscados
diretorios_para_buscar = ["Arquivos/Decretos/", "Arquivos/Leis/", "Arquivos/Outros/", "Arquivos/Portarias/"]

# Realiza a busca
resultados = buscar_pdfs(diretorios_para_buscar)

# Exibe os resultados
for diretorio, arquivos in resultados.items():
    print(f"Diretório: {diretorio}")
    if isinstance(arquivos, list):
        if arquivos:
            print("Arquivos PDF encontrados:")
            for arquivo in arquivos:
                print(f"  - {arquivo}")
        else:
            print("  Nenhum arquivo PDF encontrado.")
    else:
        print(f"  {arquivos}")
