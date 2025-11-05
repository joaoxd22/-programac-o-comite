def main():
    invertida = ""
    palavra = str(input("insira uma palavra -> "))
    for letra in palavra:
        invertida = letra + invertida
    print(invertida)

main()