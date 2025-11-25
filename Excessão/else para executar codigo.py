def dividir():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
    else:
        with open("resultado_q7.txt", "w") as arq:
            arq.write(f"Resultado da divisão: {resultado}")
        print("Divisão realizada! Resultado salvo no arquivo.")


def main():
    dividir()

main()