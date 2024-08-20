# Definição do nó na lista ligada
class AcaoPeça:
    def __init__(self, descrição, peça):
        self.descrição = descrição  # Descrição da ação (e.g., "adicionar", "remover")
        self.peça = peça  # Peça sendo adicionada ou removida
        self.próximo = None  # Referência para a próxima ação na lista ligada
        self.anterior = None  # Referência para a ação anterior na lista ligada

# Definição do sistema de estoque de peças com funcionalidade de desfazer/refazer
class EstoquePeças:
    def __init__(self):
        self.início = None  # Referência para o início da lista (primeira ação)
        self.atual = None  # Referência para a ação atual na lista ligada (última ação)
        self.estoque = []  # Armazena o estado atual do estoque

    # Método para adicionar uma nova ação ao sistema
    def nova_ação(self, descrição, peça):
        nova_ação = AcaoPeça(descrição, peça)  # Cria um novo nó (ação) com a descrição e a peça fornecidas
        if self.início is None:  # Se não há ações na lista (primeira ação)
            self.início = nova_ação  # Define esta ação como a primeira da lista
            self.atual = nova_ação  # A ação atual também passa a ser esta, já que é a única
        else:
            nova_ação.anterior = self.atual  # Liga a nova ação à ação atual, estabelecendo o vínculo anterior
            self.atual.próximo = nova_ação  # Atualiza a ação atual para apontar para a nova ação
            self.atual = nova_ação  # Move a referência da ação atual para a nova ação
        if descrição == "adicionar":
            self.estoque.append(peça)
        elif descrição == "remover":
            if peça in self.estoque:
                self.estoque.remove(peça)

    # Método para desfazer a última ação realizada
    def desfazer(self):
        if self.atual is None:  # Se não há ações para desfazer (lista vazia ou no início)
            print("Nada para desfazer")
            return

        # Exibe qual ação está sendo desfeita
        print(f"Desfazendo: {self.atual.descrição} '{self.atual.peça}'")
        if self.atual.descrição == "adicionar":
            self.estoque.remove(self.atual.peça)
        elif self.atual.descrição == "remover":
            self.estoque.append(self.atual.peça)
        self.atual = self.atual.anterior  # Move a referência da ação atual para a ação anterior

    # Método para refazer a próxima ação na lista (se houver)
    def refazer(self):
        if self.atual is None or self.atual.próximo is None:  # Se não há ações para refazer
            print("Nada para refazer")
            return

        self.atual = self.atual.próximo  # Move a referência da ação atual para a próxima ação na lista
        # Exibe qual ação está sendo refeita
        print(f"Refazendo: {self.atual.descrição} '{self.atual.peça}'")
        if self.atual.descrição == "adicionar":
            self.estoque.append(self.atual.peça)
        elif self.atual.descrição == "remover":
            self.estoque.remove(self.atual.peça)

    # Método para mostrar o estado atual do estoque, considerando as ações realizadas
    def mostrar_estoque(self):
        # Junta a lista de peças em uma string e exibe o estado atual do estoque
        print("Estado atual do estoque:", ", ".join(self.estoque))

# Exemplo de uso do sistema de estoque de peças
estoque = EstoquePeças()

# Adicionando ações (nós) na lista ligada
estoque.nova_ação("adicionar", "Roda")  # Adiciona uma roda ao estoque
estoque.nova_ação("adicionar", "Motor")  # Adiciona um motor ao estoque
estoque.nova_ação("adicionar", "Transmissão")  # Adiciona uma transmissão ao estoque
estoque.nova_ação("remover", "Roda")  # Remove uma roda do estoque
estoque.mostrar_estoque()  # Mostra o estado atual do estoque
estoque.desfazer()  # Desfaz a última ação (remover a roda)
estoque.mostrar_estoque()  # Mostra o estado atual do estoque
estoque.refazer()  # Refaz a última ação (remover a roda)
estoque.mostrar_estoque()  # Mostra o estado atual do estoque