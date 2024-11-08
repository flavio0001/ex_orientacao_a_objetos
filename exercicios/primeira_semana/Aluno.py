class Aluno():
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        media = self.calcular_media()
        if media >= 6:
            print(f"{self.nome} está aprovado! Com média: {media}")
        else:
            print(f"{self.nome} está reprovado! Com média: {media}")

aluno1 = Aluno("Julia", 7.5, 5.5)
aluno1.situacao()