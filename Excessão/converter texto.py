def converter_para_numero(texto):
    try:
        numero = float(texto)
        return f"Conversao realizada: {numero}"
    except ValueError:
        return "Erro: o texto nao pode ser convertido para numero" 

def main():
    entrada = input("Digite um número: ")
    resultado = converter_para_numero(entrada)

    with open("resultado.txt", "a") as arquivo:
        arquivo.write("Questao 4:\n")
        arquivo.write(resultado + "\n\n")

    print(resultado)

main()