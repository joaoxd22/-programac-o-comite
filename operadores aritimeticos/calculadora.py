numero_1 = int(input("me fale um numero " ))
numero_2 = int(input("me de outro numero" ))
operacao = input("me de uma operaçao" )
if operacao == "+":
    print("A SOMA É", numero_1 + numero_2)
elif operacao == "-":
    print("A SUBTRAÇÃO É ", numero_1 - numero_2)
elif operacao == "*":
    print("A MULTIPLICAÇÃO É ", numero_1 * numero_2)
elif operacao == "/":
    if numero_2 == 0:
        print("uma das condições é 0")
    else:
        resultado = numero_1 / numero_2
    print("A DIVISÃO É", resultado)
else:
    print("OPERÇÃO INVALIDA ):")