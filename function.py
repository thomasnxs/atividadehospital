import heapq

class Paciente:
    def __init__(self, nome, idade, gravidade):
        self.nome = nome
        self.idade = idade
        self.gravidade = gravidade

    def __lt__(self, other):
        return self.gravidade < other.gravidade

fila_de_prioridades = []

def listar_ultimos_chamados():
    if len(fila_de_prioridades) > 0:
        print("Os últimos 5 pacientes chamados:")
        for paciente in reversed(fila_de_prioridades[-5:]):
            print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, Gravidade: {paciente.gravidade}")
    else:
        print("Nenhum paciente foi chamado ainda.")

def mostrar_proximo_paciente():
    if len(fila_de_prioridades) > 0:
        proximo_paciente = fila_de_prioridades[0]
        print(f"Próximo paciente a ser chamado: Nome: {proximo_paciente.nome}, Idade: {proximo_paciente.idade}, Gravidade: {proximo_paciente.gravidade}")
    else:
        print("Nenhum paciente na fila.")

def atender_proximo_paciente():
    if len(fila_de_prioridades) > 0:
        proximo_paciente = heapq.heappop(fila_de_prioridades)
        print(f"Atendendo paciente: Nome: {proximo_paciente.nome}, Idade: {proximo_paciente.idade}, Gravidade: {proximo_paciente.gravidade}")
    else:
        print("Nenhum paciente na fila.")
