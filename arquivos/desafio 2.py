def boletim(nome, n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    return {
        "nome": nome,
        "n1": n1,
        "n2": n2,
        "n3": n3,
        "media": media,
        "situacao": situacao
    }

def salvar(dados):
    with open("boletim.txt", "w") as arq:
        arq.write(f"Nome: {dados['nome']}\n")
        arq.write(f"Nota 1: {dados['n1']}\n")
        arq.write(f"Nota 2: {dados['n2']}\n")
        arq.write(f"Nota 3: {dados['n3']}\n")
        arq.write(f"Media: {dados['media']:.2f}\n")
        arq.write(f"Situacao: {dados['situacao']}\n")

def main():
    nome = input("Nome do aluno: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    dados = boletim(nome, n1, n2, n3)
    salvar(dados)
    print("Boletim salvo no arquivo 'boletim.txt'!")

main()