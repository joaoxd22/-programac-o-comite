def nomes_maiusculos(lista_nomes):
    nomes_em_maiusculo = []
    for nome in lista_nomes:
        nomes_em_maiusculo.append(nome.upper())
    return nomes_em_maiusculo

def main():
    nomes = []


    print("Digite os nomes (pressione Enter sem digitar nada para parar):")
    while True:
        nome = input("Nome: ")
        if nome == "":
            break
        nomes.append(nome)
    
    resultado = nomes_maiusculos(nomes)
    
    print("Nomes em maiúsculas:")
    for nome in resultado:
        print(nome)


main()
