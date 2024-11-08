class MaquinaDeVendas:
    def __init__(self, precos):
        self.__estoque = {item: 5 for item in precos}
        self.__precos = precos
        self.__saldo_cliente = 0

    @property
    def saldo_cliente(self):
        return self.__saldo_cliente

    def ver_estoque(self):
        return self.__estoque

    def inserir_dinheiro(self, valor):
        if valor > 0:
            self.__saldo_cliente += valor
            print(f"R${valor} inserido. Saldo atual: R${self.__saldo_cliente}")
        else:
            print("Valor inválido. Por favor, insira um valor positivo.")

    def comprar_item(self, item):
        if item not in self.__estoque:
            print("Item não encontrado")
        elif self.__estoque[item] <= 0:
            print("Item esgotado no momento.")
        elif self.__saldo_cliente < self.__precos[item]:
            print(f"Saldo insuficiente para comprar {item}. Insira mais dinheiro.")
        else:
            self.__saldo_cliente -= self.__precos[item]
            self.__estoque[item] -= 1
            print(f"{item} comprado com sucesso! Saldo restante: R${self.__saldo_cliente}")

    def restituir_troco(self):
        troco = self.__saldo_cliente
        self.__saldo_cliente = 0
        print(f"Restituição de troco: R${troco}")
        return troco

    def recarregar_estoque(self, item, quantidade):
        if item in self.__estoque:
            self.__estoque[item] += quantidade
            print(f"Recarregou {quantidade} unidades de {item}. Estoque atual: {self.__estoque[item]}")
        else:
            print("Item não encontrado na máquina")

# Testando a classe MaquinaDeVendas

precos = {
    "Refrigerante": 5.0,
    "Chips": 3.5,
    "Chocolate": 4.0,
    "Água": 2.0
}

maquina = MaquinaDeVendas(precos)

print("Estoque inicial:", maquina.ver_estoque())
print("Saldo inicial do cliente:", maquina.saldo_cliente)

maquina.inserir_dinheiro(10)
maquina.comprar_item("Refrigerante")
maquina.comprar_item("Chips")

print("Saldo após compras:", maquina.saldo_cliente)
print("Estoque após compras:", maquina.ver_estoque())

maquina.restituir_troco()

maquina.inserir_dinheiro(5)
maquina.comprar_item("Chocolate")
maquina.comprar_item("Água")
maquina.comprar_item("Refrigerante")

print("Estoque final:", maquina.ver_estoque())
print("Saldo final do cliente:", maquina.saldo_cliente)
