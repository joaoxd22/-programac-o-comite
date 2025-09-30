saldo = 5000
valor_saque = 1

while valor_saque != 0:
    valor_saque = float(input("informe o valor do saque"))
    saldo -= valor_saque
    print(f"seu saldo é {saldo}")