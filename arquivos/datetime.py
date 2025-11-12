from datetime import datetime


def gera_logs():
    with open ("log.txt","w") as arquivo:
        for i in range(3):
            agora = datetime.now()
            arquivo.write(f"{agora} log {i+1} \n")

    print("log gerado com sucesso!!!")


def main():
    gera_logs()

main()