from operator import attrgetter
from functools import total_ordering

@total_ordering
class ContaSalario:
	def __init__(self, codigo):
		self._codigo = codigo
		self._saldo = 0

	def deposita(self, valor):
		self._saldo += valor

	def __eq__(self, outro): # eq (equals) define o funcionamento do == para a classe
		if type(outro) != ContaSalario: # retorna falso se os tipos não são iguais
			return False
		return self._codigo == outro._codigo and self._saldo == outro._saldo # compara o codigo e o saldo das duas classes e retorna True se forem iguais
		
	def __lt__(self, outro): # lt (less-then) define o funcionamento do < para a classe
		if self._saldo != outro._saldo:
			return self._saldo < outro._saldo # retorna True se o _saldo for menor do que o _saldo do objeto comparado.
		return self._codigo < outro._codigo # se o _saldo forem iguais, compara o _codigo e retorna True

	def __str__(self):
		return "[Código: {}\tSaldo: {}]".format(self._codigo, self._saldo)

conta1 = ContaSalario(1700)
conta1.deposita(500)

conta2 = ContaSalario(3)
conta2.deposita(1000)

conta3 = ContaSalario(133)
conta3.deposita(500)

contas = [conta1, conta2, conta3]

for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")): # attrgetter suporta mais de um parametro, primeiro ordena por _saldo e depois por _codigo.
	print(conta)
print("")

# o exemplo acima compromente o encapsulamento. 

for conta in sorted(contas):
	print(conta)
print("")

#testes
print (conta1 < conta2)
print (conta1 <= conta2)
print (conta1 <= conta3)
print (conta1 < conta1)
print (conta1 > conta1)
print (conta1 == conta1)
print (conta1 >= conta1)
print (conta1 <= conta1)