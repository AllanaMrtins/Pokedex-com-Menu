from pokedex import Pokedex
from menu import Menu

def main():
   
    controll = Pokedex()
    Menu.tela_inicial()

    while True:
        Menu.mostar_logo()
        Menu.mostrar_menu()

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            controll.consultar_pk()
        elif opcao == "2":
            controll.listar()
        elif opcao == "3":
            controll.exibir_dados()
        elif opcao == "4":
            controll.exibir_imagem()
        elif opcao == "5":
            controll.quantidade()
        elif opcao == "0":
            Menu.tela_saida()
            break
        else:
            Menu.erro("Opção inválida.")

if __name__ == "__main__":
    main()