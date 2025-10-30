def fato (numero):
    fat = 1
    for n in range (1, numero +1):
        fat *= n

    return fat



def main ():
    n = int(input("informe um numero: "))
    print(f"o fatorial do numero é {fato(n)}")

main()

 
