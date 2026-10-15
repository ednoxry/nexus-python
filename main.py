
import os
import sys
import platform
import secrets
import string


def limpar():
    os.system("clear" if os.name == "posix" else "cls")


def titulo():
    print("\033[96m")
    print(r"""
 _   _ _____  __  __ _   _ ____  
| \ | | ____| \ \/ /| | | / ___| 
|  \| |  _|    \  / | | | \___ \ 
| |\  | |___   /  \ | |_| |___) |
|_| \_|_____| /_/\_\ \___/|____/ 
    """)
    print("\033[0m")
    print("        NEXUS TOOLS • PYTHON CLI\n")


def pausar():
    input("\nPressione ENTER para continuar...")


def gerar_senha():
    try:
        tamanho = int(input("Tamanho da senha (mínimo 8): "))
        if not 8 <= tamanho <= 128:
            print("Escolha um tamanho entre 8 e 128.")
            return

        caracteres = string.ascii_letters + string.digits + "!@#$%&*?"
        senha = "".join(
            secrets.choice(caracteres) for _ in range(tamanho)
        )
        print(f"\nSua senha gerada:\n{senha}")
    except ValueError:
        print("Digite um número válido.")


def calculadora():
    try:
        a = float(input("Primeiro número: "))
        operador = input("Operador (+, -, *, /): ").strip()
        b = float(input("Segundo número: "))

        if operador == "+":
            resultado = a + b
        elif operador == "-":
            resultado = a - b
        elif operador == "*":
            resultado = a * b
        elif operador == "/":
            if b == 0:
                print("Não é possível dividir por zero.")
                return
            resultado = a / b
        else:
            print("Operador inválido.")
            return

        print(f"\nResultado: {resultado}")
    except ValueError:
        print("Digite números válidos.")


def analisar_texto():
    texto = input("Digite ou cole seu texto: ")
    palavras = texto.split()

    print("\n--- ANÁLISE ---")
    print(f"Caracteres: {len(texto)}")
    print(f"Caracteres sem espaços: {len(texto.replace(' ', ''))}")
    print(f"Palavras: {len(palavras)}")
    print(f"Linhas: {len(texto.splitlines()) or 1}")


def informacoes():
    print("\n--- SISTEMA ---")
    print(f"Sistema: {platform.system()}")
    print(f"Versão: {platform.release()}")
    print(f"Arquitetura: {platform.machine()}")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Plataforma: {platform.platform()}")


def menu():
    while True:
        limpar()
        titulo()
        print("[1] Gerar senha")
        print("[2] Calculadora")
        print("[3] Analisar texto")
        print("[4] Informações do sistema")
        print("[0] Sair")

        opcao = input("\nNEXUS > ").strip()

        if opcao == "1":
            gerar_senha()
        elif opcao == "2":
            calculadora()
        elif opcao == "3":
            analisar_texto()
        elif opcao == "4":
            informacoes()
        elif opcao == "0":
            print("\nObrigado por usar o NEXUS Tools!")
            break
        else:
            print("Opção inválida.")

        if opcao != "0":
            pausar()


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nPrograma encerrado.")

