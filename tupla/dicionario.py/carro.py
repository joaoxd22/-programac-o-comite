carro = {
    "marca": "chevrolett",
    "modelo": "s10",
    "ano": "2023"
}

print(carro["marca"])
  
carro ['cor'] = "branco"
print(carro)
for chave , valor in carro.items():
    print(f" a chave é {chave} o valor é {valor}")


carro ["ano"] = "2025"
del carro ["modelo"]
print(carro.get("modelo"))

for chave , valor in carro.items():
    print(f" a chave é {chave} o valor é {valor}")

#############################

for chave in carro.keys():
    print(chave)

for valor in carro.values():
    print(valor)

for chave, valor in carro.items():
    print(f"Chave: {chave}, Valor: {valor}")


    ##################
carro = {
     "marca": "chevrolett",
    "modelo": "s10",
    "ano": "2023"
}

for chave, valor in carro.items():
    print(f"Chave: {chave}, Valor: {valor}")

