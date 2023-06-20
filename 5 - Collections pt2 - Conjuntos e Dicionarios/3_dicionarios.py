aparicoes = {
	"Manga" : 1,
	"Banana" : 2,
	"Cavalo" : 2,
	"Urso": 1
}

print(aparicoes)
print(type(aparicoes))

aparicoes["Camelo"] = 1 # inclui Camelo no dicionário
print(aparicoes)

aparicoes["Camelo"] = 2 # substitui o valor de Camelo para 2
print(aparicoes)

del aparicoes["Camelo"] # remove Camelo do dicionário
print(aparicoes)

print("Urso" in aparicoes) # procura se a chave "Urso" esta no dicionário
print("Camelo" in aparicoes) # procura se a chave "Camelo" esta no dicionário
print("")

for elemento in aparicoes: # iterando para "printar" elementos do dicionário
	print(elemento)
print("")

for elemento in aparicoes.keys(): # iterando com base nas chaves do dicionário
	print(elemento)
print("")

for elemento in aparicoes.values(): # iterando com base nos valores das chaves do dicionário
	print (elemento)
print("")

for elemento in aparicoes.items(): # iterando com base nos items do dicionário (retorna uma tupla (chave, valor))
	print(elemento)
print("")

for chave, valor in aparicoes.items(): # iterando com base nos items do dicionário unpacking tuplas
	print(chave, valor)