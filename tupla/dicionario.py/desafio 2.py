alunos = {}

while True:
    nome = input("Nome do aluno (ou 'sair' para terminar): ")
    if nome == 'sair':
        break
    idade = int(input("Idade: "))
    nota = float(input("Nota: "))
    
    alunos[nome] = {'idade': idade, 'nota': nota}

if len(alunos) > 0:
    soma_notas = 0
    maior_nota = -1
    melhor_aluno = ''

    for nome in alunos:
        nota = alunos[nome]['nota']
        soma_notas += nota
        if nota > maior_nota:
            maior_nota = nota
            melhor_aluno = nome

    media = soma_notas / len(alunos)
    
    print("\n--- RESULTADOS ---")
    print("Média das notas:", media)
    print("Aluno com a maior nota:", melhor_aluno, "- Nota:", maior_nota)
else:
    print("Nenhum aluno cadastrado.")

