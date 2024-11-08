class Carro:
    def __init__(self, marca, modelo, velocidade=0):
        self._marca = marca
        self._modelo = modelo
        self._velocidade = velocidade

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    def aumentar_velocidade(self, valor):
        nova_velocidade = self._velocidade + valor
        if nova_velocidade > 180:
            self._velocidade = 180
        else:
            self._velocidade = nova_velocidade
        print(f"Velocidade atual: {self._velocidade} km/h")

    def reduzir_velocidade(self, valor):
        nova_velocidade = self._velocidade - valor
        if nova_velocidade < 0:
            self._velocidade = 0
        else:
            self._velocidade = nova_velocidade
        print(f"Velocidade atual: {self._velocidade} km/h")

    @property
    def velocidade(self):
        return self._velocidade


# Testando a classe Carro

carro1 = Carro("Toyota", "Corolla")

print("Marca inicial:", carro1.marca)
print("Modelo inicial:", carro1.modelo)

carro1.marca = "Honda"
carro1.modelo = "Civic"
print("Nova marca:", carro1.marca)
print("Novo modelo:", carro1.modelo)

carro1.aumentar_velocidade(50)
carro1.aumentar_velocidade(100)
carro1.aumentar_velocidade(50)

carro1.reduzir_velocidade(30)
carro1.reduzir_velocidade(150)

print("Velocidade final:", carro1.velocidade)
