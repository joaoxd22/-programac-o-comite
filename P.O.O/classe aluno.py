class Aluno:
    def __init__(self, nota1=0, nota2=0):
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2


def salvar_notas(n1, n2):
    with open("q7_aluno.txt", "w") as arq:
        arq.write(f"{n1}\n{n2}\n")


def carregar_notas():
    try:
        with open("q7_aluno.txt", "r") as arq:
            linhas = arq.readlines()
            n1 = float(linhas[0].strip())
            n2 = float(linhas[1].strip())
            return n1, n2
    except:
        return None


def menu():
    print("\n===== MENU DO ALUNO =====")
    print("1 - Registrar notas")
    print("2 - Ver notas")
    print("3 - Ver média")
    print("4 - Sair")
    print("=========================")


def main():
    while True:
        menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            print("\n--- Registrar Notas ---")
            n1 = float(input("Digite a nota 1: "))
            n2 = float(input("Digite a nota 2: "))
            salvar_notas(n1, n2)
            print("Notas registradas com sucesso!")

        elif opc == "2":
            print("\n--- Ver Notas ---")
            dados = carregar_notas()
            if dados:
                print(f"Nota 1: {dados[0]}")
                print(f"Nota 2: {dados[1]}")
            else:
                print("Nenhuma nota registrada ainda.")

        elif opc == "3":
            print("\n--- Média do Aluno ---")
            dados = carregar_notas()
            if dados:
                aluno = Aluno(dados[0], dados[1])
                print(f"Média: {aluno.calcular_media():.2f}")
            else:
                print("Registre as notas primeiro.")

        elif opc == "4":
            print("\nSaindo... Até a próxima!")
            break

        else:
            print("Opção inválida! Tente novamente.")


main()