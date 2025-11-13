import os

def listar_arquivos():
    arquivos = os.listdir(".")
    print("Arquivos da pasta atual: ")
    for arquivo in arquivos:
        print(arquivo)

def main():
    listar_arquivos()

main()