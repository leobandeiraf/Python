class bomba_combustivel:
  def __init__(self, tipo_combustivel, quantidade_combustivel):
    self.valor_litro = 3.52    

    self.tipo_combustivel = tipo_combustivel
    self.quantidade_combustivel = quantidade_combustivel
    

  def abastecer_por_valor(self, valor):
    self.quantidade_combustivel = self.quantidade_combustivel + (valor / self.valor_litro)

    return print(f"Foi adicionado no total: {valor / self.valor_litro} litro(s) ao seu veículo.\nTotalizando: {self.quantidade_combustivel}L")

  def abastecer_por_litro(self, litro):
    valor_pago = 0

    valor_pago += litro * self.valor_litro

    return print(f"O valor total por {litro}L é de: R${valor_pago}\nTotalizando: {self.quantidade_combustivel + litro}L")

  def alterar_valor(self, valor):
    self.valor_litro = valor

    return print(f"O valor do litro foi atualizado para: R${self.valor_litro}")

  def alterar_tipo_combustivel(self, tipo_combustivel):
    self.tipo_combustivel = tipo_combustivel

    return print(f"O tipo de combustível foi alterado para: {self.tipo_combustivel}")

  def alterar_quantidade_combustivel(self, quantidade_combustivel):
    self.quantidade_combustivel = quantidade_combustivel

    return print(f"A quantidade de combustível restante na bomba foi atualizado para: {self.quantidade_combustivel}L")

bomba1 = bomba_combustivel("normal", 5)
#bomba1.abastecer_por_valor(35.2)
#bomba1.abastecer_por_litro(5)
#bomba1.alterar_valor(2.55)
#bomba1.abastecer_por_litro(5)
#bomba1.alterar_tipo_combustivel("aditivado")
#bomba1.alterar_quantidade_combustivel(6)
#bomba1.abastecer_por_valor(35.2)