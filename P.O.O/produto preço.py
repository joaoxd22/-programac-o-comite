class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


def salvar_produto(produto):
    with open("q4_produto.txt", "w") as arq:
        arq.write(f"Nome: {produto.nome}\n")
        arq.write(f"Preço: {produto.preco}\n")


def main():
    print("=== QUESTÃO 4 ===")

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))

    produto = Produto(nome, preco)

    salvar_produto(produto)

    print("Produto salvo no arquivo q4_produto.txt")


main()