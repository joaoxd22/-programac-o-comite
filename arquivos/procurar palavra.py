def procurar_palavra(nome_arquivo, palavra):
    with open(nome_arquivo, "r") as arquivo:
        texto = arquivo.read()
        if palavra in texto:
            print("A palavra foi encontrada no arquivo.")
        else:
            print("A palavra não foi encontrada no arquivo.")

def main():
    arquivo = "nome_arquivo"
    palavra = input("Digite a palavra que deseja procurar: ")
    procurar_palavra(arquivo, palavra)

main()