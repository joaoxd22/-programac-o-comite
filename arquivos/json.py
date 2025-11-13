import json
def jason():
    dados = {"nome": "joao", "idade": 17}
    with open ("dados.json", "w") as f:
        json.dump(dados, f, indent = 4)