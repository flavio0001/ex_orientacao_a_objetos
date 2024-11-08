class Funcionario:
    def __init__(self, nome, cargo, salario):
        self._nome = nome
        self._cargo = cargo
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, novo_cargo):
        self._cargo = novo_cargo

    @property
    def salario(self):
        return self._salario

    def aumentar_salario(self, percentual):
        novo_salario = self._salario * (1 + percentual / 100)
        return novo_salario

# Exemplos de uso

funcionario = Funcionario("João", "Analista", 2600)
print("Salário atual:", funcionario.salario)

novo_salario = funcionario.aumentar_salario(30)
print("Novo salário com aumento de 30%:", novo_salario)

funcionario.cargo = "Gerente"
funcionario.nome = "João Silva"
print("Novo cargo:", funcionario.cargo)
print("Novo nome:", funcionario.nome)
