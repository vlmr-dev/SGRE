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

# Funcionalidade 02
def exibir_estudantes():
    for estudante in estudantes:
        print(f"Nome: {estudante['nome']}, ID: {estudante['id']}, Notas: {', '.join(map(str, estudante['notas']))}")

# Funcionalidade 03
def procurar_por_id():
    id_procurado = input("Digite o ID do estudante que deseja procurar: ")
    for estudante in estudantes:
        if estudante['id'] == id_procurado:
            print(f"Estudante encontrado - Nome: {estudante['nome']}, ID: {estudante['id']}, Notas: {', '.join(map(str, estudante['notas']) )}")
            return
    print("Estudante com ID informado não encontrado.")

estudantes = []

criar_arquivo()

while True:
    print("")
    print("| SISTEMA DE GERENCIAMENTO DE REGISTROS DE ESTUDANTES |")
    print("")
    print("1. Adicionar Registro de Estudante")
    print("2. Exibir Registros de Estudantes")
    print("3. Procurar por um Estudante")
    print("4. Sair")
    print("")

    opcao = input("Digite sua escolha (1 - 4): ")

    if opcao == "1":
        adicionar_estudante()
    elif opcao == "2":
        exibir_estudantes()
    elif opcao == "3":
        procurar_por_id()    
    elif opcao == "4":
        print("Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")