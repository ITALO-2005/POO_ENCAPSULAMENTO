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
        return self.id_funcionario

    def calcular_salario(self):
        return self.salario_base + self.bonus - (self.faltas * 100)  # Penalidade de 100 por falta

    def resumo(self):
        return (f"Nome: {self.nome}\n"
                f"ID: {self.id_funcionario}\n"
                f"Salário Base: R$ {self.salario_base:.2f}\n"
                f"Bônus: R$ {self.bonus:.2f}\n"
                f"Faltas: {self.faltas}\n"
                f"Salário Final: R$ {self.calcular_salario():.2f}")