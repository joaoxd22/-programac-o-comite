lista_original = [1, 2, 3 ,4, 5 ,6 ,7 ,8 , 9 ,10]
lista_pares = []

for numero in lista_original:
    if numero % 2 == 0:
        lista_pares.append(numero)

print("lista original:", lista_original)
print("lista de numeros pares:", lista_pares)
