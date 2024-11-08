class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"carro: {self.marca} | {self.modelo} | ano: {self.ano}")

carro1 = Carro("Volvo", "SUV", 2017)
carro2 = Carro("McLaren", "720S", 2023)
carro1.exibir_informacoes()
carro2.exibir_informacoes()