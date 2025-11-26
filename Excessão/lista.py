def ler_lista():
    lista = [10, 20, 30]

    try:
        indice = int(input("Digite o índice (0 a 2): "))
        print("Valor:", lista[indice])
    except IndexError:
        print("Erro: índice fora da lista.")

def main():
    ler_lista()

main()