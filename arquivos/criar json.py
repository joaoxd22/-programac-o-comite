import json

def main():
    dados_pessoais = {
        "nome": "João",
        "idade": 17,
        "cidade": "sapucaia",
        "profissão": "Estudante"
    }

    try:
        with open("pessoais.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados_pessoais, arquivo, indent=4, ensure_ascii=False)

        print("Arquivo 'pessoais.json' criado com sucesso!")

    except Exception as erro:
        print(f"Ocorreu um erro ao criar o arquivo: {erro}")

main()