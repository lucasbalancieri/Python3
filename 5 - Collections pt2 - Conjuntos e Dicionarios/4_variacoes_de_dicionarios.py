from collections import defaultdict
from collections import Counter

meu_texto = "Bem vindo meu nome é Lucas eu gosto muito de nomes e tenho meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()


aparicoes = {} #dict vazio

for palavra in meu_texto.split():
	ate_agora = aparicoes.get(palavra, 0) # get busca a chave (palavra) no dicionário e retona o valor, se a palavra não existir, retorna 0
	aparicoes[palavra] = ate_agora + 1
print(aparicoes)

print("")

aparicoes = defaultdict(int) 
# toda vez que a chave buscada no dicinário não existir, a busca retornará 0
# a função int usada como parametro é uma função que retorna 0 por padrão
# quando a chave não está no dicionário, o defaultdict chama o que foi passado no parametro.

for palavra in meu_texto.split():
	ate_agora = aparicoes[palavra]
	aparicoes[palavra] = ate_agora + 1
print(aparicoes)

print("")

aparicoes = Counter(meu_texto.split()) # função de collections utilizada como contador, recebe um iterável e o conta
print(aparicoes)





