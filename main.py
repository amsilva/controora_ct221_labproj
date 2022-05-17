from entidades import Pessoa
from entidades import Atividade

a1 = Pessoa("Fulano", 1001)
fulano_palestra = Atividade("palestra", 10)
fulano_certificado = Atividade("certificacao", 40)
fulano_filme = Atividade("filme cinema", 4)
fulano_filme2 = Atividade("filme netflix", 4)
fulano_voluntariado = Atividade("voluntariado", 40)
a1.atividades.append(fulano_palestra)
a1.atividades.append(fulano_certificado)
a1.atividades.append(fulano_filme)
a1.atividades.append(fulano_filme2)
a1.atividades.append(fulano_voluntariado)
fulano_palestra.aprova()
fulano_certificado.aprova()


a2 = Pessoa("Beltrano", 1002)
beltrano_curso = Atividade("curso", 200)
beltrano_certificado = Atividade("certificacao", 400)
a2.atividades.append(beltrano_curso)
a2.atividades.append(beltrano_certificado)
beltrano_curso.aprova()

a3 = Pessoa("Cicrano", 1003)

turma = []
turma.append(a1)
turma.append(a2)
turma.append(a3)

#dashboard
for aluno in turma :
	print(f"[{aluno.registro}] {aluno.nome} : ", end="")
	tot = 0
	for evento in aluno.atividades :
		tot = tot + evento.getCarga()
	print(tot, "h")	



