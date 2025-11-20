def abrir_arquivo():
    try:
        nome = input("Digite o nome do arquivo para abrir: ")
        with open(nome, "r") as arq:
            conteudo = arq.read()
        return f"Conteúdo do arquivo:\n{conteudo}\n"
    except FileNotFoundError:
        return "Erro: O arquivo informado nao foi encontrado.\n"

def main():
    resultado = abrir_arquivo()

    with open("resultado_q3.txt", "w") as arquivo:
        arquivo.write(resultado)

    print("Processo concluído! Resultado salvo em resultado_q3.txt")

main()