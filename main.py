import random
import heapq
from function import Paciente, listar_ultimos_chamados, mostrar_proximo_paciente, atender_proximo_paciente, fila_de_prioridades



for _ in range(10):
    nome = f"Paciente {random.randint(1, 100)}"
    idade = random.randint(1, 100)
    gravidade = random.randint(1, 10)
    paciente = Paciente(nome, idade, gravidade)
    heapq.heappush(fila_de_prioridades, paciente)


while True:
    print("\nOpções:")
    print("1. Listar os 5 últimos pacientes chamados")
    print("2. Mostrar o próximo paciente sem chamar")
    print("3. Atender o próximo paciente")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        listar_ultimos_chamados()
    elif escolha == "2":
        mostrar_proximo_paciente()
    elif escolha == "3":
        atender_proximo_paciente()
    elif escolha == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")

print("Jogo encerrado.")
