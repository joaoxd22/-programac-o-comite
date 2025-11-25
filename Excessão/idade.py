def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa.")
    return idade


def main():
    try:
        idade = int(input("Digite a idade: "))
        verificar_idade(idade)

        with open("resultado_q9.txt", "w") as arq:
            arq.write(f"Idade válida: {idade}")

        print("Idade válida! Salva no arquivo.")

    except ValueError as erro:
        print(erro)

main()