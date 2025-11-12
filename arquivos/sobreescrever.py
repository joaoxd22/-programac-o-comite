def sobrescrever_arquivo(nome_arquivo,novo_texto):
    with open ("nome_arquivo","w") as arquivo:
        arquivo.write(novo_texto)

def main():
    arquivo = "arquivo.txt"
    texto = input("digite um novo texto para o aquivo !!! ")
    sobrescrever_arquivo(arquivo, texto)
    print("arquivo sobrescrito com sucesso !!! ")

main()