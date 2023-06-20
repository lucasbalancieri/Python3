from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
	def test_quando_idade_recebe_13_03_2001_deve_retornar_22(self):
		entrada = '13/03/2001' # Given (contexto)
		esperado = 22

		funcionario_teste = Funcionario('Teste', entrada, 1111)
		resultado = funcionario_teste.idade() # When (ação)

		assert resultado == esperado # Then (desfeco)

	def test_quando_sobrenome_receber_Gary_Oak_deve_retornar_Oak(self):
		entrada = " TesteNome TesteSobrenome " # Given
		esperado = "TesteSobrenome"

		ash = Funcionario(entrada, '11/11/2001', 1111)
		resultado = ash.sobrenome() # When

		assert resultado == esperado # Then

	def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
		entrada_salario = 100000 # Given
		entrada_nome = 'Bragança'
		esperado = 90000

		funcionario_teste = Funcionario(entrada_nome, '11/11/2001', entrada_salario)
		funcionario_teste.decrescimo_salario() # When
		resultado = funcionario_teste.salario

		assert resultado == esperado # Then

	@mark.calcular_bonus
	def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
		entrada = 1000
		esperado = 100

		funcionario_teste = Funcionario('teste', '11/11/20', entrada)
		resultado = funcionario_teste.calcular_bonus()

		assert resultado == esperado

	@mark.calcular_bonus
	def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exception(self):
		with pytest.raises(Exception):
			entrada = 10000000 # Given

			funcionario_teste = Funcionario('teste', '11/11/20', entrada)
			resultado = funcionario_teste.calcular_bonus() # When

			assert resultado # Then

