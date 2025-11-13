import shutil

def copiar_arquivo():
  try:
    origem = "arq1.txt"
    destino = "copia_arq1.txt"

    shutil.copy(origem,destino)
    print(f"Arquivo {origem} copiado com sucesso para {destino} !!! ")
  except Exception as erro:
    print(f"Ocorreu um erro {erro}")

def main():
  copiar_arquivo()

main()
