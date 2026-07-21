class Produto:
    contador_id = 1

    def __init__(self, nome, preco, quantidade):
        self.id = Produto.contador_id
        Produto.contador_id += 1

        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

    def calcular_valor_total(self):
        return self.preco * self.quantidade


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def buscar_produto(self, id_produto):
        for produto in self.produtos:
            if produto.id == id_produto:
                return produto

        return None

    def remover_produto(self, id_produto):
        produto = self.buscar_produto(id_produto)

        if produto:
            self.produtos.remove(produto)
            return True

        return False

    def listar_produtos(self):
        if not self.produtos:
            print("\nNenhum produto cadastrado.")
            return

        for produto in self.produtos:
            print(
                f"\nID: {produto.id}"
                f"\nNOME: {produto.nome}"
                f"\nPREÇO: R${produto.preco:.2f}"
                f"\nQUANTIDADE: {produto.quantidade}"
            )
            print("-" * 30)

    def calcular_valor_total_estoque(self):
        return sum(produto.calcular_valor_total() for produto in self.produtos)


def menu():
    estoque = Estoque()

    while True:
        print("""
========= CONTROLE DE ESTOQUE =========

1. Adicionar Produto
2. Listar Produtos
3. Buscar Produto
4. Remover Produto
5. Atualizar Quantidade
6. Valor total do estoque
0. Sair

========================================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))

            produto = Produto(nome, preco, quantidade)

            estoque.adicionar_produto(produto)

            print("\nProduto adicionado com sucesso!")


        elif opcao == "2":
            estoque.listar_produtos()


        elif opcao == "3":
            id_produto = int(input("Digite o ID do produto: "))

            produto = estoque.buscar_produto(id_produto)

            if produto:
                print(
                    f"\nID: {produto.id}"
                    f"\nNOME: {produto.nome}"
                    f"\nPREÇO: R${produto.preco:.2f}"
                    f"\nQUANTIDADE: {produto.quantidade}"
                )
            else:
                print("\nProduto não encontrado.")


        elif opcao == "4":
            id_produto = int(input("Digite o ID do produto: "))

            if estoque.remover_produto(id_produto):
                print("\nProduto removido com sucesso!")
            else:
                print("\nProduto não encontrado.")


        elif opcao == "5":
            id_produto = int(input("Digite o ID do produto: "))

            produto = estoque.buscar_produto(id_produto)

            if produto:
                nova_quantidade = int(
                    input("Digite a nova quantidade: ")
                )

                produto.atualizar_quantidade(nova_quantidade)

                print("\nQuantidade atualizada com sucesso!")

            else:
                print("\nProduto não encontrado.")


        elif opcao == "6":
            valor_total = estoque.calcular_valor_total_estoque()

            print(
                f"\nValor total do estoque: R${valor_total:.2f}"
            )


        elif opcao == "0":
            print("\nEncerrando programa...")
            break


        else:
            print("\nOpção inválida!")


menu()

