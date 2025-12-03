def pegar_num(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("Digite um número válido.")

def registrar(txt):
    with open("historico.txt", "a") as arq:
        arq.write(txt + "\n")

def calcular():
    while True:
        op = input("\nOperação (+ - * /) ou 'sair': ").lower()

        if op == "sair":
            break
        if op not in ["+", "-", "*", "/"]:
            print("Opção inválida.")
            continue

        n1 = pegar_num("1º valor: ")
        n2 = pegar_num("2º valor: ")

        try:
            resultado = eval(f"{n1}{op}{n2}")
        except ZeroDivisionError:
            print("Erro: divisão por zero.")
            continue

        print("Resultado:", resultado)
        registrar(f"{n1} {op} {n2} = {resultado}")

def main():
    calcular()

main()