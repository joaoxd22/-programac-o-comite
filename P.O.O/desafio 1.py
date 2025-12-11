class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} - {self.autor} ({status})"


class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar(self, titulo, usuario):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"📚 {usuario.nome} pegou o livro '{titulo}'.")
                else:
                    print(f"❌ O livro '{titulo}' já está emprestado.")
                return
        print(f"❌ Livro '{titulo}' não encontrado.")

    def devolver(self, titulo, usuario):
        for livro in self.livros:
            if livro.titulo == titulo:
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"🔄 {usuario.nome} devolveu o livro '{titulo}'.")
                else:
                    print(f"❌ O livro '{titulo}' já está na biblioteca.")
                return
        print(f"❌ Livro '{titulo}' não encontrado.")


# ------------ Função principal ------------
def main():
    biblioteca = Biblioteca()

    # Criando 5 livros
    livros = [
        Livro("Dom Casmurro", "Machado de Assis"),
        Livro("O Alienista", "Machado de Assis"),
        Livro("Capitães da Areia", "Jorge Amado"),
        Livro("O Pequeno Príncipe", "Saint-Exupéry"),
        Livro("1984", "George Orwell")
    ]

    for l in livros:
        biblioteca.adicionar_livro(l)

    # Criando 3 usuários
    u1 = Usuario("Ana")
    u2 = Usuario("Carlos")
    u3 = Usuario("Beatriz")

    # Simulações
    biblioteca.emprestar("1984", u1)
    biblioteca.emprestar("Dom Casmurro", u2)
    biblioteca.emprestar("1984", u3)  # já emprestado

    biblioteca.devolver("1984", u1)
    biblioteca.emprestar("1984", u3)  # agora disponível


# Executar programa
main()