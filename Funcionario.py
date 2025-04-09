class Funcionario:
    def __init__(self, nome, id_funcionario, salario_base):
        self.nome = nome
        self.id_funcionario = id_funcionario
        self.salario_base = salario_base
        self.bonus = 0
        self.faltas = 0

    def registrar_falta(self):
        self.faltas += 1

    def adicionar_bonus(self, valor):
        self.bonus += valor

    def recalcular_bonus(self):
        penalidade = self.faltas * 50
        self.bonus = max(0, self.bonus - penalidade)  
    
    def get_id(self):
        return id_funcionario

    def 

        