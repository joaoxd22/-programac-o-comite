def calculadora(numero1 , numero2, operaçao):
    if operaçao == "+":
        resultado = numero1 + numero2
    elif operaçao == "-":
        resultado = numero1 - numero2
    elif operaçao == "*":
        resultado = numero1 * numero2
    elif operaçao == "/":
        resultado = numero1 / numero2
    else:
        resultado = "operação invalida"
    print(f"resultado: {resultado}")

def main():
    while True:
        op = input("digite a operação (+,-,*,/) ou sair para encerrar: " )
        if op == 'sair':
            print("encerrando calculadora")
            break
        n1 = float(input("digite o primeiro numero -> "))
        n2 = float(input("digite o segundo numero -> "))
        calculadora (n1,n2,op)

main()