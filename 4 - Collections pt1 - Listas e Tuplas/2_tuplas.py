
class ContaConrrente:
	def __init__(self, codigo):
		self.codigo = codigo
		self.saldo = 0

	def deposita(self, valor):
		self.saldo += valor

	def __str__(self):
		return "[Código: {}\tSaldo: {}]".format(self.codigo, self.saldo)


conta1 = ContaConrrente(15)
conta2 = ContaConrrente(47685)

conta1.deposita(500)
conta2.deposita(1000)

contas = [conta1, conta2]
for conta in contas:
	print(conta)

user_conta1 = ('User1', 37, 1981) # tupla
user_conta2 = ('User2', 31, 1987)
