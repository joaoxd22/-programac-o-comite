class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


def salvar_area(area):
    with open("retangulo.txt", "w") as arq:
        arq.write(f"Área do retângulo: {area}\n")


def main():
    largura = float(input("Largura: "))
    altura = float(input("Altura: "))

    r = Retangulo(largura, altura)
    resultado = r.area()

    salvar_area(resultado)
    print("Área salva no arquivo retangulo.txt")