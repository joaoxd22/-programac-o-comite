def boletim(nome, n1, n2, n3):
    media = (n1 + n2 + n3)/ 3
    if media >= 7:
        situação = "aprovado"
    else:
        situação = "reprovado"
    aluno= {"nome": nome, "media": media, "situação": situação}
    print(aluno)

def main():
    nome = input('digite o nome do aluno: ')
    nota1 = float(input("digite a primeira nota do aluno: "))
    nota2 = float(input("digite a segunda nota do aluno: "))
    nota3 = float(input("digite a terceira nota do aluno: "))
    resultado = boletim(nome,nota1,nota2,nota3)
    print(resultado)

main()