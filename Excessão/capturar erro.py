def executar_operacao(valor):
    try:
        r = 100 / float(valor)
        return f"Resultado: {r}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

def main():
    entrada = input("Digite um número: ")
    resultado = executar_operacao(entrada)

    with open("resultado.txt", "a") as arquivo:
        arquivo.write("Questão 6:\n")
        arquivo.write(resultado + "\n\n")

    print(resultado)

main()