class Livro:
    def __init__(self, titulo, autor, paginas, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponibilidade = disponibilidade
    def empLivro(self):
        if self.disponibilidade == True:
            self.disponibilidade = False
    def devLivro(self):
        if self.disponibilidade == False:
            self.disponibilidade = True