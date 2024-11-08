class MaquinaDeCafe:
    def __init__(self, agua, cafe, copos):
        self.__agua = agua
        self.__cafe = cafe
        self.__copos = copos

    @property
    def agua(self):
        return self.__agua

    @property
    def cafe(self):
        return self.__cafe

    @property
    def copos(self):
        return self.__copos

    def fazer_cafe(self):
        if self.__agua < 200:
            print("Água insuficiente para fazer um café.")
        elif self.__cafe < 15:
            print("Café insuficiente para fazer um café.")
        elif self.__copos < 1:
            print("Copos insuficientes para servir o café.")
        else:
            self.__agua -= 200
            self.__cafe -= 15
            self.__copos -= 1
            print("Café feito com sucesso!")

    def recarregar_agua(self, quantidade):
        self.__agua += quantidade
        print(f"Recarregou {quantidade} ml de água. Total de água: {self.__agua} ml")

    def recarregar_cafe(self, quantidade):
        self.__cafe += quantidade
        print(f"Recarregou {quantidade} g de café. Total de café: {self.__cafe} g")

    def recarregar_copos(self, quantidade):
        self.__copos += quantidade
        print(f"Recarregou {quantidade} copos. Total de copos: {self.__copos}")

# Testando a classe MaquinaDeCafe

maquina = MaquinaDeCafe(agua=500, cafe=100, copos=5)

print("Estoque inicial de água:", maquina.agua)
print("Estoque inicial de café:", maquina.cafe)
print("Estoque inicial de copos:", maquina.copos)

maquina.fazer_cafe()
maquina.fazer_cafe()
maquina.fazer_cafe()

maquina.recarregar_agua(300)
maquina.recarregar_cafe(50)
maquina.recarregar_copos(10)

maquina.fazer_cafe()
maquina.fazer_cafe()
maquina.fazer_cafe()

print("Estoque final de água:", maquina.agua)
print("Estoque final de café:", maquina.cafe)
print("Estoque final de copos:", maquina.copos)
