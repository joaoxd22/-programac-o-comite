def maior_elemento(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

def main():
    numeros = [3, 7, 2, 9, 5] 
    print("A lista é:", numeros)
    print("O maior elemento é:", maior_elemento(numeros))

main()
