from random import randrange

class Pet():  
  fome_limite = 5
  saude_limite = 25
  idade_limite = 100 

  fome_decremento = 1
  saude_incremento = 1
  idade_incremento = 1

  def __init__(self, nome):
    self.nome = nome
    self.fome = randrange(self.fome_limite)
    self.saude = randrange(self.saude_limite)
    self.idade = 1

  def __str__(self):
    status = f"Meu nome é {self.nome}, tenho {self.idade} ano(s) de idade.\nMeu nível de fome é {self.fome}.\nMeu nível de saúde é {self.saude}."

    return status
      
  def humor(self):
    if self.fome <= self.fome_limite and self.saude >= self.saude_limite:
      return "feliz"
    elif self.fome > self.fome_limite:
      return "faminto"
    else:
      return "mal"

  def oi(self): 
    print(f"Olá! Eu sou {self.nome}, tenho {self.idade} ano(s) e estou me sentindo {self.humor()}.")
    self.saude += 1

  def alterar_nome(self, nome):
    self.nome = nome

    return print(f"Olá! Me chame agora de {self.nome}.")

  def alimentar(self, vezes):
    self.reduzir_fome(vezes)

  def brincar(self, pergunta):
    self.aumentar_saude(pergunta)

  def crescer(self):
    self.aumentar_idade()

  def reduzir_fome(self, vezes):
    for i in range(vezes):
      self.fome -= self.fome_decremento

  def aumentar_saude(self, tempo):
    for i in range(tempo):
      self.saude += self.saude_incremento

  def aumentar_idade(self):
    self.idade += 1

  def tick_tack(self):
    self.fome += 1
    self.saude -= 1

zaja = Pet("Zaja")
zaja.oi()
for i in range(2):
  zaja.tick_tack()
zaja.alimentar(2)
zaja.oi()
for i in range(23):
  zaja.tick_tack()
zaja.oi()
zaja.brincar(21)
zaja.alimentar(20)
zaja.oi()
zaja.aumentar_idade()
zaja.oi()
zaja.alterar_nome("Tulipa")
zaja.oi()
print(zaja)