from operator import attrgetter


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
	
	def __lt__(self, outro): # retorna True se o _saldo for menor do que o _saldo do objeto comparado.
		return self._saldo < outro._saldo

	def __str__(self):
		return "[Código: {}\tSaldo: {}]".format(self._codigo, self._saldo)

conta1 = ContaSalario(17)
conta1.deposita(500)

conta2 = ContaSalario(3)
conta2.deposita(1000)

conta3 = ContaSalario(133)
conta3.deposita(510)

contas = [conta1, conta2, conta3]
def extrai_saldo(conta):
	return conta._saldo

for conta in sorted(contas, key=extrai_saldo):
	print(conta)
print("")
# o exemplo acima funciona porém não é uma boa pratica pois, apesar de funcionar, a função extrai_saldo 
# acessa o atributo privado _saldo da classe ContaSalario.

for conta in sorted(contas, key=attrgetter("_saldo")):
	print(conta)
print("")
# esse exemplo também funciona, no entanto, continua a não ser uma boa pratica pois ainda acessa o atributo 
# privado _saldo da classe, comprometendo o encapsulamento.

# OBS: os exemplos acima podem ser aplicados em outras situações! # 

print(conta1 < conta2) # o < funciona pois foi implementado através do __lt__ na classe
print(conta1 > conta2)
print("")

for conta in sorted(contas):
	print(conta)
print("")

for conta in sorted(contas, reverse=True):
	print(conta)
