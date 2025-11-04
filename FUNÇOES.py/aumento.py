def calcular_aumento(valor, porcentagem):
    aumento = valor * (porcentagem / 100)
    valor_final = valor + aumento
    return valor_final

def main():
    valor = float(input("Digite o valor: "))
    porcentagem = float(input("Digite a porcentagem de aumento: "))
    
    resultado = calcular_aumento(valor, porcentagem)
    
    print(f"O valor com aumento é: {resultado:.2f}")

main()
