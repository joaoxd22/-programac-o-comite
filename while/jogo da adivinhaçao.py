import random
numero_secreto = random.randint(1, 100)
tentativas = 0

print("bem vindo ao jogo de adivinhaçao")
print("tente adivinhar o numero secreto entre 1 e 100. ")
while True:
    try:
        chute = int(input("qual é o seu chute: "))
        tentativas += 1

        if chute < numero_secreto:
            print("seu chute foi muito baixo.")
        elif chute > numero_secreto:
            print("seu chute foi muito alto")
        else:
            print(f"parabens. voce acertou o numero secreto ({numero_secreto}) em {tentativas} tentativas ")
            break
    except ValueError:
        print("entrada invalida. por favor digite um numero inteiro. ")
