class Animal:
    def fazer_som(self):
        return "Som genérico de animal"


def salvar_som(som):
    with open("q8_som.txt", "w") as arq:
        arq.write(f"Som produzido: {som}\n")


def main():
    print("=== QUESTÃO 8 ===")

    animal = Animal()
    som = animal.fazer_som()

    salvar_som(som)

    print("Som salvo no arquivo q8_som.txt")


main()