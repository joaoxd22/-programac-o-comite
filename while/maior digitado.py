numero = 1
maior_numero = 0

while numero != 0:
    numero = int(input("informe um numero"))

    if numero > maior_numero:
        maior_numero = numero

print(f" o maior numero e {maior_numero}") 