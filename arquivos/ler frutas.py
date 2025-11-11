try:
    with open("arquivo_frutas.txt","r") as arquivo:
     frutas = arquivo.readlines()

    fruta = [frutas.strip()for fruta in frutas]

    print(frutas)

except FileNotFoundError:
   print("o arquivo nao foi encontrado :( )")
except Exception as erro:
   print(f"ocorreu um erro{erro}")