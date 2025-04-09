func = Funcionario("João Silva", 123, 2000)
func.registrar_falta()
func.adicionar_bonus(500)
func.recalcular_bonus()
print(func.resumo())

from funcionario import Funcionario

departamento = []
func1 = Funcionario("Ana Silva", "F001", 3000)
departamento.append(func1)

func1.adicionar_bonus(500)
print(func1.resumo())

func1.registrar_falta()
func1.registrar_falta()
print(func1.resumo())
