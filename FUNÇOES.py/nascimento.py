def calcular_idade(ano_nascimento):
    ano_atual = 2025
    idade = ano_atual - ano_nascimento
    return idade
def main():
    nascimento = int(input("digite su ano de nascimento -> "))
    idade = calcular_idade(nascimento)
    print(f"sua idade é {idade}")

main()