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

	def __str__(self):
		return "[Código: {}\tSaldo: {}]".format(self._codigo, self._saldo)


conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

print(conta1)
print(conta2)

print('São iguais?', conta1 == conta2)
print('São diferentes?', conta1 != conta2)