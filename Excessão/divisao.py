def dividir():
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 / n2
        return f"Resultado da divisao: {resultado}\n"
    except ZeroDivisionError:
        return "Erro: Nao e possivel dividir por zero.\n"
    except ValueError:
        return "Erro: Digite somente números.\n"

def main():
    texto = dividir()

    with open("resultado_q2.txt", "w") as arquivo:
        arquivo.write(texto)

    print("Processo concluído! Resultado salvo em resultado_q2.txt")

main()