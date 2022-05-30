class Pessoa :
	
	def __init__(self, n, r) :
		self.nome = n
		self.registro = r
		self.atividades = [] #lista de atividades realizadas

	def getTotalCarga(self) :
		tot = 0
		for evento in self.atividades :
			tot = tot + evento.getCarga()
		return tot	
		
		

class Atividade :
	
	def __init__(self, titulo, duracao) :
		self.titulo = titulo
		self.duracao = duracao
		self.estado = 1 #nova

	def getCarga(self) :
		if self.estado == 4 : #aprovada
			return self.duracao
		else :
			return 0
		
	def aprova(self) :
		#if self.estado == 2 : ##TODO incluir o teste de pendencia
		self.estado = 4 

