def criar_arquivos():
  try:
    for i in range (1, 6):
      nome_arquivo = f"arq{i}.txt"
      with open (nome_arquivo,"w") as arquivo:
        arquivo.write(f"Arquivo numero {i}\n")
    print("arquivos criados com sucesso !!! ")
  except Exception as erro:
    print(f"Aconteceu um erro {erro}")


def main():
  criar_arquivos()

main()