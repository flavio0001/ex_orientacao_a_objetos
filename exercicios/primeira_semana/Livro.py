class Livro():
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_informacoes(self):
        print(f"Título do livro: {self.titulo} | Autor: {self.autor} | Publicado em: {self.ano_publicacao}")


livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
livro2 = Livro("1984", "George Orwell", 1949)

livro1.exibir_informacoes()
livro2.exibir_informacoes()