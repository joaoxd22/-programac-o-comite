# ----- Função para salvar no arquivo -----
def salvar_arquivo_carro(texto):
    with open("carro.txt", "w", encoding="utf-8") as arq:
        arq.write(texto)

# ----- Classe Carro -----
class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        return f"O carro {self.modelo} ({self.ano}) está ligado!"

# ----- Função principal -----
def main():
    modelo = input("Digite o modelo do carro: ")
    ano = input("Digite o ano do carro: ")

    carro = Carro(modelo, ano)
    mensagem = carro.ligar()
    print(mensagem)

    salvar_arquivo_carro(mensagem)
    print("Mensagem salva no arquivo carro.txt")

main()
