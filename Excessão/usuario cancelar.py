def somar():
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print("Soma =", a + b)
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")

def main():
    somar()

main()