class Animal:
    def fazer_som(self):
        return "Som de animal"


class Gato(Animal):
    def fazer_som(self):
        return "Miau!"


class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"


def salvar_sons(som_gato, som_cachorro):
    with open("q9_animais.txt", "w") as arq:
        arq.write(f"Gato: {som_gato}\n")
        arq.write(f"Cachorro: {som_cachorro}\n")


def main():
    print("=== QUESTÃO 9 ===")

    gato = Gato()
    cachorro = Cachorro()

    som_gato = gato.fazer_som()
    som_cachorro = cachorro.fazer_som()

    salvar_sons(som_gato, som_cachorro)

    print("Sons salvos no arquivo q9_animais.txt")


main()