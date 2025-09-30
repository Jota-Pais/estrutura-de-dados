class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def media(self):
        media = (self.nota1 + self.nota2) / 2
        if media >= 6:
            aprovado = True
        else:
            aprovado = False
        print( media, aprovado)
        
aluno1 = Aluno('João', 7, 8)
aluno2 = Aluno('Maria', 5, 6)

aluno1.media()
aluno2.media()    
    
    
    
   