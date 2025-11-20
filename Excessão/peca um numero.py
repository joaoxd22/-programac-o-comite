def main():
    try:
        numero = int(input("Digite um número: "))
        print("Você digitou:", numero)
    except ValueError:
        print("Erro: você deve digitar apenas números inteiros.")

main()