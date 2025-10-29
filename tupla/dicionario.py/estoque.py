estoque = {
    "caderon": 10,
    "lapis": 5,
    "mochila": 15}

print("estoque atualizado")
for chave, valor in estoque.items():
    print(f"produto - {chave} | qtd produto - {valor}")

estoque.update({"mochila": 20, "caderno":50, "caderno": 0 })
print("vendas efetuadas com sucesso! ")

print("estoque atualizado")
for chave, valor in estoque.items():
    print(f"produto - {chave} | qtd produto - {valor}")

estoque['regua'] = 10
for chave, valor in estoque.items():
     print(f"produto - {chave} | qtd produto - {valor}")
print("removendo um produto")
del estoque ["lapis"]

print("estoque atualizado")
for chave, valor in estoque.items():
     print(f"produto - {chave} | qtd produto - {valor}")
    
print('limpando estoque')
estoque.clear()
print(f"estoque limpo.{estoque}")

