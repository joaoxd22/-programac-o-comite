import random
opçao = ()
candidatos=[]
while (opçao != 0):
    opçao = int(input("oq deseja fazer? \n"\
                      "opção 1 : Cadastrar um candidato: \n" \
                      "opção 2 : fazer sua votação: \n" \
                      "opção 0 : sair: \n\n" \
                      "opção -> :"))
    if opçao == 1:
        while True:
            candidato_temp = []
            nome = input ("informe o nome do seu candidato -> ")
            voto = int(input("insira o numero do seu candidato desejado -> "))
            candidato_temp.append(nome)
            candidato_temp.append(voto)
            candidatos.append(candidato_temp)
            continuar = input("deseja contimuar S para sim ou N para não ")
            if continuar != ("s"):
                break
    elif opçao == 2:
        while True:
            chave = ""
            for linha in candidatos:
                for coluna in linha:
                    chave += str(coluna)
                    print(chave)
            break   





