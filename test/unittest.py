
## Teste basico para entidade PESSOA
##
def test_PessoaBasico(self):
  p = Pessoa("ABC", 123)
  #p.nome = "ABC"
  #p.registro = 123
  self.assertEquals(p.nome, "ABC")
  self.assertEquals(p.registro, 123)

## Teste de inicializacao
##
def test_AtividadeInicializacao(self):
  a = Atividade("TESTE", 100)
  self.assertEquals(a.titulo, "TESTE")
  self.assertEquals(a.duracao, 100)
  self.assertEquals(a.estado, 1) #NOVA

## Teste de manipulacao de carga por atividade
##
def test_AtividadeAprovacaoEGetCarga(self):
  a = Atividade("ATIVIDADE", 100)
  self.assertEquals(a.estado, 1) # NOVA
  self.assertEquals(a.getCarga(), 0) # NOVA
  a.aprova()
  self.assertEquals(a.estado, 4) # NOVA
  self.assertEquals(a.getCarga(), 100) # APROVADA


## Teste de manipulacao de carga total
##
def test_PessoaGetTotalCarga(self):
  a1 = Atividade("UM", 1)
  a2 = Atividade("DOIS", 2)
  a3 = Atividade("TRES", 3)
  p = Pessoa("PESSOA", 1)
  p.atividades.append(a1)
  p.atividades.append(a2)
  self.assertEquals(p.getTotalCarga(), 0) # NOVA
  a1.aprova()
  self.assertEquals(p.getTotalCarga(), 1) # NOVA
  a2.aprova()
  self.assertEquals(p.getTotalCarga(), 3) # NOVA
  
  p.atividades.append(a3)
  self.assertEquals(p.getTotalCarga(), 3) # NOVA

  a3.aprova()
  self.assertEquals(p.getTotalCarga(), 6) # NOVA
 
