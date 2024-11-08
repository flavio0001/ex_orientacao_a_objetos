class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

    def usar(self, consumo):
        if consumo <= self.bateria:
            self.bateria -= consumo
            print(f"Usou {consumo}% da bateria. Carga atual: {self.bateria}%")
        else:
            print("Bateria insuficiente para esse uso. Carregue o celular.")

    def carregar(self, carga):
        self.bateria += carga
        if self.bateria > 100:
            self.bateria = 100
        print(f"Carregou {carga}%. Carga atual: {self.bateria}%")

    def exibir_bateria(self):
        print(f"Bateria atual: {self.bateria}%")


celular1 = Celular("Samsung", "Galaxy S21")
celular1.usar(20)
celular1.exibir_bateria()
celular1.carregar(15)
celular1.usar(95)
celular1.exibir_bateria()
