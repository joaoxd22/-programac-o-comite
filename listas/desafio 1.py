numeros = []
for i in  range (5):
    num= float(input(f"digite o {i+1}numero:"))
    numeros.append(num)

maior_numero = max(numeros)
menor_numero = min(numeros)
media = sum(numeros)/len(numeros)

print(f"o maior número é {maior_numero}")
print(f"o menor número é {menor_numero}")
print(f"a média dos numero é {media}")