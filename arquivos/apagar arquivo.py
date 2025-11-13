import os

def apagar_arquivo(nome_arquivo):
  try:
    os.remove(nome_arquivo)
    print("arquivo apagado com sucesso!!! ")
  except FileNotFoundError:
    print("arquivo não encontrado")

def main():
  arquivo = input("digite o nome de um arquivo que deseja apagar -> ")
  apagar_arquivo(arquivo)

main()  