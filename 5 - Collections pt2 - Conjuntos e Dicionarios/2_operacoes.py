usuarios = {1, 5, 76, 34, 52, 13, 17}

print("Tamanho inicial {}\n".format(len(usuarios)))


print("Tenta .add(13)")
usuarios.add(13) # não adiciona o 13 pois ja existe no set, não retorna erro.
print("Tamanho atual: {}\n".format(len(usuarios)))

print(".add(765)")
usuarios.add(765)
print("Tamanho atual: {}\n".format(len(usuarios)))

print(usuarios)

usuarios = frozenset(usuarios) # congela o set, torna o set imutavél
print(usuarios)

meu_texto = "Meu nome é Teste e gosto muito de teste E gosto de testar e testar e Testar"
print(meu_texto.split())
print(set(meu_texto.split()))