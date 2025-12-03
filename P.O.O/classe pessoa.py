# ----- Função para salvar em arquivo -----
def salvar_em_arquivo(texto):
    with open("pessoa.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)

# ----- Classe Pessoa -----
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# ----- Função principal -----
def main():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")

    pessoa = Pessoa(nome, idade)
    mensagem = pessoa.apresentar()
    print(mensagem)

    salvar_em_arquivo(mensagem)
    print("Apresentação salva no arquivo pessoa.txt")

# Executa o programa
main()