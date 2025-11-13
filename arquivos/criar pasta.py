import os

def criar_pasta(nome_pasta):
  try:
    os.mkdir(nome_pasta)
    print(f"pasta {nome_pasta} criada com sucesso :)")
  except FileExistsError:
    print(f"a pasta {nome_pasta} já existe !!!")

def main():
    nome = input("digite o nome da nova pasta -> ")
    criar_pasta(nome)

main()