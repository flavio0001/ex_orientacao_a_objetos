class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saldacao(self):
        print(f"Olá! me chamo {self.nome} e tenho {self.idade} anos. Tudo bem?")

pessoa1 = Pessoa("júlia", 27)
pessoa2 = Pessoa("Gabriella", 24)
pessoa1.saldacao()
pessoa2.saldacao()