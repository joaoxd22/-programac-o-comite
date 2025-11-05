def contar_positivos(lista):
    contador = 0
    for numero in lista:
        if numero > 0:
            contador += 1
    print(f"quantidade de numeros positivos é -> {contador} ")
def main():
    numeros = [3, 2, -1, 4, -7, -9]
    contar_positivos(numeros)
 
main()