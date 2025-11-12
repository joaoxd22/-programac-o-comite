def gera_lista(arquivo):
   lista = []
   try:
      with open(arquivo) as arq:
         for linha in arq:
            lista.append(linha.strip())
      return lista
   except FileNotFoundError:
      print("ARQUIVO NÃO ENCONTRADO")


def main():
   lista = []
   arquivo = "frutas.txt"
   lista = gera_lista(arquivo)
   print(lista)


main()
