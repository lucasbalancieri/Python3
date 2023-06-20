usuarios_data_science = [15, 23, 43, 56] 
usuarios_machine_learning = [13, 23, 56, 42] 

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

print(set(assistiram)) 
# um set não possui index;
# não possui padrão de ordenação dos elementos;
# descarta a ocorrência de elementos duplicados

for usuario in set(assistiram):
	print(usuario)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

assistiram = usuarios_data_science | usuarios_machine_learning 
# | (ou) faz a união dos dois sets com os elementos que existem em ambos os conjuntos
print(assistiram)

assistiram = usuarios_data_science & usuarios_machine_learning
# & (e) faz a intersecção apenas dos elementos que exisem em ambos os conjuntos
print(assistiram)

assistiram = usuarios_data_science - usuarios_machine_learning 
print(assistiram)
assistiram = usuarios_machine_learning - usuarios_data_science 
print(assistiram)
# - (diferença) faz a união dos elementos que existem apenas em um set 
