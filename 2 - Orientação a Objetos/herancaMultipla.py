# Parte 2
class Funcionario:

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):

    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

jose = Junior()
# herdados da classe Funcionario
# jose.registra_horas(14)
# jose.mostrar_tarefas()
# herdados da classe Alura
# jose.busca_perguntas_sem_resposta()

luan = Pleno()
# herdados da classe Funcionario
jose.registra_horas(14)
jose.mostrar_tarefas()
# herdados da classe Alura
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()