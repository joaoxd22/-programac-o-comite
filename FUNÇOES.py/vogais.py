def contar_vogais (texto):
    vogais = ("a", "e", "i", "o", "u")
    contar_vogais = 0
    for letra in texto:
        if letra in vogais:
            contar_vogais += 1
            
    return contar_vogais

def main():
    qtd_vogais = contar_vogais(input("digite o texto -> "))
    print(f"o texto digitado tem {qtd_vogais} vogais! ")


main()