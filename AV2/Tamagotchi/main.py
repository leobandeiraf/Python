from random import randrange

class Pet():
  def __init__(self, nome):
    self.nome = nome
    self.fome = self.fome_limite
    self.saude = self.saude_limite
    self.idade = self.humor_limite 
    
    self.fome_limite = 5
    self.saude_limite = 10
    self.idade_limite = 1 

  def __str__(self):
    status = f"  Eu sou {self.nome}.\nEstou me sentindo {self.humor()}."

    return status
      
  def humor(self):
    if self.fome <= self.fome_limite and self.saude <= self.saude_limite:
      return "feliz"
    elif self.fome > self.fome_limite:
      return "faminto"
    else:
      return "mal"

  def alterar_nome(self, nome):
    self.nome = nome

    return print(f"Olá! Me chame agora de {self.nome}.")


Zaja = Pet(Zaja)
Zaja = 
