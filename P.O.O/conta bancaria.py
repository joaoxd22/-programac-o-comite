# ----- Função para salvar no arquivo -----
def salvar_arquivo_conta(texto):
    with open("conta_bancaria.txt", "a", encoding="utf-8") as arq:
        arq.write(texto + "\n")

# ----- Classe ContaBancaria -----
class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}"

    def sacar(self, valor):
        if valor > self.saldo:
            return "Erro: saldo insuficiente!"
        self.saldo -= valor
        return f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}"

# ----- Função principal -----
def main():
    saldo_inicial = float(input("Digite o saldo inicial: "))
    conta = ContaBancaria(saldo_inicial)

    valor_deposito = float(input("Digite o valor para depósito: "))
    msg1 = conta.depositar(valor_deposito)
    print(msg1)
    salvar_arquivo_conta(msg1)

    valor_saque = float(input("Digite o valor para saque: "))
    msg2 = conta.sacar(valor_saque)
    print(msg2)
    salvar_arquivo_conta(msg2)

    print("Operações salvas no arquivo conta_bancaria.txt")

main()