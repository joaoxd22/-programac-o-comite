class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        return self.preco


def salvar_desconto(produto):
    with open("q5_desconto.txt", "w") as arq:
        arq.write(f"Produto: {produto.nome}\n")
        arq.write(f"Preço final após desconto: {produto.preco}\n")


def main():
    print("=== QUESTÃO 5 ===")

    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    percentual = float(input("Percentual de desconto (%): "))

    produto = Produto(nome, preco)
    produto.aplicar_desconto(percentual)

    salvar_desconto(produto)

    print("Desconto aplicado e salvo no arquivo q5_desconto.txt")



main()