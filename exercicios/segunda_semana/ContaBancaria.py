class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self._titular = titular
        self._saldo = saldo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor >= 0:
            self._saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso")
        else:
            print("O valor deve ser positivo")

    def sacar(self, valor):
        if valor >= 0:
            if valor <= self._saldo:
                self._saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso")
            else:
                print("Saldo insuficiente para realizar o saque")
        else:
            print("O valor de saque deve ser positivo")


# Testando a classe
conta1 = ContaBancaria("Carlos", 1000)

print("Titular:", conta1.titular)
print("Saldo inicial:", conta1.saldo)

conta1.depositar(50)
print("Conta após depósito:", conta1.saldo)

conta1.sacar(50)
print("Após saque:", conta1.saldo)
