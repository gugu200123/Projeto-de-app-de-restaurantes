import os

restaurantes = [{"nome":"Burguer King","categoria":"Fast Food","ativo":False}, 
                {"nome":"MCdonalds","categoria":"Fast Food","ativo":True}]

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
    linha = "*" (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    subtitulo("Cadastrar novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseje cadastrar: \n")
    categoria = input(f"Digite a categoria do restaurante {nome_restaurante} :")
    dados_do_restaurante = {"nome":nome_restaurante,"categoria":categoria,"ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"\nO restaurante {nome_restaurante} foi cadastrado com sucesso\n")
    voltar_menu()

def listar_restaurante():
    subtitulo("Listando os restaurantes")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f"{nome_restaurante} | {categoria} | {ativo}")
    voltar_menu()

def ativar_restaurante():
    subtitulo("Alternando o estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado :")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_menu()

def escolher_opção():
    try:
        opcao =int(input("Escolha uma opção : "))
        if opcao == 1:
            cadastrar_restaurante()

        elif opcao == 2:
            listar_restaurante()

        elif opcao == 3:
            ativar_restaurante()

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