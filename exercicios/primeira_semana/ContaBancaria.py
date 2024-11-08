class ContaBancaria():
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depositou R${valor}. Novo saldo: R${self.saldo}")


    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Sacou R${valor}. Novo saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo}. ")


conta1 = ContaBancaria("Carlos")
conta1.depositar(100)
conta1.sacar(30)
conta1.exibir_saldo()