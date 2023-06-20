from collections import Counter


texto1 = """
	insira o texto aqui.
"""


texto2 = """
	insira o texto aqui.
"""

def analisa_frequencia_de_letras(texto):
	aparicoes = Counter(texto.lower()) # dicionário das aparições do texto1
	total_de_caracteres = sum(aparicoes.values()) # total de caracteres do texto1
	#print('Total de letras no texto1: {}'.format(total_de_caracteres))

	# frequencia de todas as letras do texto1
	'''
	for letra, frequencia in aparicoes.items():
		tupla = (letra, frequencia/total_de_caracteres)
		print (tupla)
	'''

	proporcoes = [(letra, frequencia/total_de_caracteres) for letra, frequencia in aparicoes.items()] # list comprehension do for acima
	# para cada letra (key) busca a frequência (value) em aparecições 
	#> coloca na tupla 
	#> processa proporcao através de frequencia/total_de_caracteres 
	#> coloca a tupla na lista proporcoes.

	proporcoes = Counter(dict(proporcoes))
	mais_comuns = proporcoes.most_common(10)
	for caractere, proporcao in mais_comuns:
		print('{} x {:.2f}%'.format(caractere, proporcao * 100))
	#for chave, valor in proporcoes.items():
	
print("texto1:")
analisa_frequencia_de_letras(texto1)
print("texto2:")
analisa_frequencia_de_letras(texto2)
	
