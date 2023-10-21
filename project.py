# -*- coding: utf-8 -*-
import os

def criar_arquivo():
    try:
        sgre_directory = os.path.expanduser("~/SGRE")
        if not os.path.exists(sgre_directory):
            os.makedirs(sgre_directory)
        arquivo_path = os.path.join(sgre_directory, "registros.txt")


        with open(arquivo_path, "x") as arquivo:
            print("Arquivo 'registros.txt' criado com sucesso.")
    except FileExistsError:
        print("O arquivo 'registros.txt' já existe.")

# Funcionalidade 01
def adicionar_estudante():
    nome = input("Digite o nome do estudante: ")
    id_estudante = input("Digite o ID do estudante: ")
    notas = input("Digite as notas do estudante (separadas por espaço): ").split()
    notas = [float(nota) for nota in notas]
    estudantes.append({"nome": nome, "id": id_estudante, "notas": notas})

estudantes = []

criar_arquivo()

while True:
    print("")
    print("| SISTEMA DE GERENCIAMENTO DE REGISTROS DE ESTUDANTES |")
    print("")
    print("1. Adicionar Registro de Estudante")
    print("2. Sair")
    print("")

    opcao = input("Digite sua escolha (1 - 2): ")

    if opcao == "1":
        adicionar_estudante()
    elif opcao == "2":
        print("Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")