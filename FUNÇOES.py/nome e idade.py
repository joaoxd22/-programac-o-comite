def criar_frase(nome, idade):
    frase = f"Olá, {nome}! Você tem {idade} anos."
    return frase

def main():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    resultado = criar_frase(nome, idade)
    print(resultado)

main()
