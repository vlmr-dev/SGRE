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

estudantes = []

criar_arquivo()

while True:
    print("")
    print("| SISTEMA DE GERENCIAMENTO DE REGISTROS DE ESTUDANTES |")
    print("")
    print("1. Sair")
    print("")

    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        print("Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")