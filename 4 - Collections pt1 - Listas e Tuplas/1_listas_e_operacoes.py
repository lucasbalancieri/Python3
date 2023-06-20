# listas e operações

idades = [39, 30, 27, 18]
print(idades)

for idade in idades:	# passar por todos os elementos da lista
	print(idade)

idades.append(15)	# adiciona o elemento na última posição da lista
idades.append(30)
print(idades)

idades.remove(30)	# remove a primeira ocorrência do elemento
print(idades)

idades.clear()	# limpa a lista
print(idades)

idades = [20, 39, 18]
print(idades)

idades.insert(0, 28)	# insere o elemento 28 na posição 0 da lista
idades.extend([27, 19])	# extende a lista com os elementos do iteravel passado como parâmetro
print(idades)

idades = [20, 39, 18, 27, 19]
idades_no_ano_que_vem = []
for idade in idades:
	idades_no_ano_que_vem.append(idade+1)

print(idades)
print(idades_no_ano_que_vem)

# exemplos list comprehension
idades_no_ano_que_vem_lc = [idade+1 for idade in idades]
print(idades_no_ano_que_vem_lc)

idades_no_ano_que_vem_lc = [idade for idade in idades if idade > 21]
print(idades_no_ano_que_vem_lc)

def proximo_ano(idade):
	return idade+1

idades_no_ano_que_vem_lc = [proximo_ano(idade) for idade in idades]
print(idades_no_ano_que_vem_lc)



