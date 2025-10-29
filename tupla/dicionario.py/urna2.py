opcao = -1
senha_encerrar = 1903
encerrar_votaçao = 1900
candidatos = []
contagem_votos = {"nulos" : 0}

#menu principal
while opcao != senha_encerrar:
    opcao = input(" O que deseja fazer? \n"
                  "opção 1: cadastrar candidato \n"
                  "opçao 2: iniciar votação \n"
                  "opçao 3: mostrar votos e vencedor \n"
                  "opção -> ")
    
    #valida se a opção é um numero
    if opcao.isdigit():
        opcao = int(opcao)

        #teste para opção da urna
        if opcao == 1:
            qtd_candidatos = int(input("quantos candidatos"
                                       "deseja cadastrar"))
            
            #laço para cadastrar o candidato
            for c in range (1 , qtd_candidatos):
                candidato = []
                nome_candidato = input(f"nome do candidato {c+1}")
                num_candidato = int(input(f"numero do candidato {c} -> "))

                #salva candidato
                candidato.append(nome_candidato)
                candidato.append(num_candidato)

                #salva candidato na lista principal
                candidato.append(tuple(candidato))

            print("\n\n")

        elif opcao == 2:
            voto = -1
            while voto != encerrar_votaçao:
                for candidato in candidatos:
                    print(f"candidato {candidato[0]} | numero {candidato[0]}")

                voto = int(input("vote no numero de candidato -> "))
                cont = 0
                for candidato in candidatos:
                    cont += 1
                    if voto == candidato[1]:
                        if candidato[0] not in contagem_votos.keys:
                            contagem_votos.update ({candidatos[0]: 1})
                            break
                    else:
                        if cont == len (candidatos):
                            contagem_votos["nulos"] += 1

        elif opcao == 3:
            contagem_votos["nulos"] -=1


            maior = 0
            vencedor = ""
            for key,value in contagem_votos.items():
                if value > maior:
                    maior = value
                    vencedor = key
                print(f"{key} | votos {value}")
            
            print(f"o vencedor é {vencedor} com {maior} votos")

    else:
        print("\n \nOpçao invalida\n\n")

                            
        