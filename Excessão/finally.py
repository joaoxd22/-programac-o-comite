def ler_numero():
    try:
        numero = int(input("Digite um número: "))
        print(f"Você digitou: {numero}")
    except ValueError:
        print("Erro: valor inválido.")
    finally:
        with open("resultado_q8.txt", "w") as arq:
            arq.write("Programa encerrado")
        print("Programa encerrado (mensagem salva no arquivo).")


def main():
    ler_numero()

main()
