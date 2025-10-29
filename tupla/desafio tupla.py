tupla_com_repeticao = (1, 2, 2, 3, 4, 4, 5, 1)

numeros_unicos_lista = []
for numero in tupla_com_repeticao:

    if numero not in numeros_unicos_lista:
 
        numeros_unicos_lista.append(numero)

tupla_unica = tuple(numeros_unicos_lista)

print (*tupla_com_repeticao)
print(tupla_unica)
