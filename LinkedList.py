import LinkedList

def main():
    texto_editor = LinkedList.EditorTexto()  # Create an instance of EditorTexto

    while True:
        print("1. Adicionar caractere")
        print("2. Desfazer ação")
        print("3. Refazer ação")
        print("4. Mostrar estado atual")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            descricao = "adicionar"
            valor = input("Digite o caractere a ser adicionado: ")
            texto_editor.nova_acao(descricao, valor)
        elif choice == "2":
            texto_editor.desfazer()
        elif choice == "3":
            texto_editor.refazer()
        elif choice == "4":
            texto_editor.mostrar_estado()
        elif choice == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()