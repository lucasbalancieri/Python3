idades = [15, 87, 32, 65, 56, 32, 49, 37]
usuarios = [("user1", 37, 1981), ("user2", 31, 1987), ("user3", 39, 1979)]

print(idades)
print(sorted(idades)) # ordena a lista do menor para o maior
print(list(reversed(idades))) # inverte a lista sem ordenar
print(sorted(idades, reverse=True)) # inverte e ordena a lista através do parametro reverse de sorted
print(list(reversed(sorted(idades)))) # ordena a lista através do sorted, inverte a lista através do reversed
# os exemplos acima não alteram a lista idade, o sorted retorna uma nova lista e o reversed retorna um 
# iterável que será armazenado em uma lista através do construtor da classe list()
idades.sort()
print(idades)
