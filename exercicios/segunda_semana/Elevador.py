class Elevador:
    def __init__(self, total_andares, capacidade):
        self.__andar_atual = 0
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__pessoas_presentes = 0

    @property
    def andar_atual(self):
        return self.__andar_atual

    @property
    def pessoas_presentes(self):
        return self.__pessoas_presentes

    def entrar(self):
        if self.__pessoas_presentes < self.__capacidade:
            self.__pessoas_presentes += 1
            print(f"Uma pessoa entrou! Pessoas no elevador: {self.__pessoas_presentes}")
        else:
            print("Elevador cheio! Não é possível entrar")

    def sair(self):
        if self.__pessoas_presentes > 0:
            self.__pessoas_presentes -= 1
            print(f"Uma pessoa saiu! Pessoas no elevador: {self.__pessoas_presentes}")
        else:
            print("Elevador vazio! Não há ninguém para sair")

    def subir(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
            print(f"O elevador subiu para o andar {self.__andar_atual}")
        else:
            print("O elevador já está no último andar")

    def descer(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
            print(f"O elevador desceu para o andar {self.__andar_atual}")
        else:
            print("O elevador já está no térreo")

# Testando a classe Elevador

elevador = Elevador(total_andares=5, capacidade=3)

print("Andar inicial:", elevador.andar_atual)
print("Pessoas no elevador:", elevador.pessoas_presentes)

elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.entrar()

elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()

elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()

elevador.sair()
elevador.sair()
elevador.sair()
elevador.sair()

print("Andar final:", elevador.andar_atual)
print("Pessoas no elevador:", elevador.pessoas_presentes)
