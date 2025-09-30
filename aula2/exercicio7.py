class Paciente:
    def __init__(self, nome, idade, historico):
        self.nome = nome
        self.idade = idade
        self.historico = historico
    def addConsulta(self, consulta):
        self.historico.append(consulta)
    def mostraHistorico(self):
        for consulta in self.historico:
            print(consulta)
jonas = Paciente('jonas', 20, ['consulta1','consulta2'])
jonas.addConsulta('consulta3')
jonas.mostraHistorico()