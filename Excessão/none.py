def abrir_arquivo():
    nome = input("Digite o nome do arquivo: ")

    try:
        with open(nome, "r") as arq:
            print("Arquivo aberto com sucesso!")
            return arq.read()
    except:
        print("Erro ao abrir o arquivo.")
        return None

def main():
    conteudo = abrir_arquivo()
    print("Retorno da função:", conteudo)

main()