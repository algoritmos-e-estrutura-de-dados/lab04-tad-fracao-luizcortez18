# TAD
# Tipo Abstrato de Dados
def mdc(a,b):
  while b != 0:
    r = a%b
    a = b
    b = r
  return a
class Fracao:  
  numerador = 1
  denominador = 1
#init = iniciando a classe
  def __init__(self, numerador, denominador):
    self.numerador = numerador
    self.denominador = denominador

  def add(self, fracao):#self palavra reservada
    num = (self.numerador * fracao.denominador) + \
     (fracao.numerador * self.denominador)
    dem = self.denominador * fracao.denominador
    return Fracao(num, dem)

  def sub(self, fracao):
     num = (self.numerador * fracao.denominador) - \
     (fracao.numerador * self.denominador)
     dem = self.denominador * fracao.denominador
     return Fracao(num, dem)
    

  def mul(self, fracao):
    num = self.numerador * fracao.numerador
    dem = fracao.denominador * self.denominador
    return Fracao(num, dem)

  def solve(self):
    return self.numerador/self.denominador
  
  def __str__(self):
    return f"{self.numerador}/{self.denominador}"

  def simplify(self):
    if self.numerador == 0:
      return f"{int(self.numerador)}/{int(self.denominador)}"
    elif self.denominador == 0:
      return f"{self.numerador}"
    else:
      d = mdc(self.numerador,self.denominador)
      return f"{int(self.numerador//d)}/{int(self.denominador//d)}"

    
#instanciando objeto    
    
fracao1= Fracao(9,3)
fracao2= Fracao(10,5)
fracao3= fracao1.add(fracao2)
fracao4= fracao1.sub(fracao2)
fracao5= fracao1.mul(fracao2)

print(f"fracao1: {fracao1.simplify()}")
print(f"fracao2: {fracao2.simplify()}")
print(f"fracao3: {fracao3.simplify()}")
print(f"fracao4: {fracao4.simplify()}")
print(f"fracao5: {fracao5.simplify()}")

  


  