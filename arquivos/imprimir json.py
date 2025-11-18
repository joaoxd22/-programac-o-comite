import json

def main():
    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

    except FileNotFoundError:
        print("Erro: O arquivo 'dados.json' não foi encontrado.")

    except json.JSONDecodeError:
        print("Erro: O arquivo não está em formato JSON válido.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

main()