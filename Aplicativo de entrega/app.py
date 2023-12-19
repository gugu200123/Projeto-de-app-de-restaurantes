import os

restaurantes = ["Burguer King", "MCdonalds"]

def exibir_menu():
    print("APP DE ENTREGA\n")

    print("1- Cadastrar restaurante")
    print("2- Listar Restaurante")
    print("3- Ativar restaurante ")
    print("4- SAIR\n")

def voltar_menu():
    input("\nDigite uma tecla para voltar ao menu principal.\n")
    main()

def sair_do_programa():
    os.system("cls")
    print("Saindo do programa\n")

def opcao_invalida():
    print("Opcao invalida!!!")
    voltar_menu()

def subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

def cadastrar_restaurante():
    subtitulo("Cadastrar novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseje cadastrar: \n")
    restaurantes.append(nome_restaurante)
    print(f"\nO restaurante {nome_restaurante} foi cadastrado com sucesso\n")
    voltar_menu()

def listar_restaurante():
    subtitulo("Listando os restaurantes")
    for restaurante in restaurantes:
        print(f"{restaurante}")
    voltar_menu()

def escolher_opção():
    try:
        opcao =int(input("Escolha uma opção : "))
        if opcao == 1:
            cadastrar_restaurante()

        elif opcao == 2:
            listar_restaurante()

        elif opcao == 3:
            print("Ativar restaurante")

        elif opcao == 4: 
            sair_do_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main ():
    os.system("cls")
    exibir_menu()
    escolher_opção()

if __name__ == "__main__":
    main()