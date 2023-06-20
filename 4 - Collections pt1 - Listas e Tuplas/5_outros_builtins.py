idades = [15, 87, 32, 65, 56, 32, 49, 37]
print (range(len(idades)))

for i in range(len(idades)):
	print (i, idades[i])

print(list(enumerate(idades)))

for valor in enumerate(idades): # retorna os pares em tuplas
	print(valor)

for indice, idade in enumerate(idades): # unpacking da tupla
	print(indice, idade)

usuarios = [("user1", 37, 1981), ("user2", 31, 1987), ("user3", 39, 1979)]

for nome, _, _ in usuarios: # unpacking da tupla discartando o restante além do nome
	print(nome)