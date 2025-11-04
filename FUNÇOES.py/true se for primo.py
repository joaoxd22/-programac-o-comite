def eh_primo(num):
    if num <= 1:
        return False
    for i in range (2,num):
        if num % i == 0:
            return False
    return True
def main():
    n = int(input("digite um numero -> "))
    print(eh_primo(n))

main()
