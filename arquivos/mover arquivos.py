import shutil
import os

def mover_arquivo():
  try:
    origem = "copia_arq1.txt"
    destino_pasta = "pasta_destino"

    if not os.path.exists(destino_pasta):
      os.mkdir(destino_pasta)


    shutil.move(origem, destino_pasta)
    print(f"Arquivo {origem} movido com sucesso para a pasta {destino_pasta}")
  except Exception as erro:
    print(f"Ocorreu um erro {erro} !!! ")

def main():
  mover_arquivo()

main()
