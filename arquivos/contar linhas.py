def contar_linhas(nome_arquivo):
  try:
    with open ("nome_arquivo", "r") as arquivo:
        linhas = arquivo.readlines()
        return len(linhas)
  except FileNotFoundError:
     print("ARQUIVO NÃO ENCONTRADO")
     return 0

    
def main():
    arquivo = "arquivo.txt"
    quantidade = contar_linhas (arquivo)
    if quantidade > 0:
        print(f"o arquivo tem {quantidade} linhas")

main()