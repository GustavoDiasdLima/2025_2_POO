from models.cliente import Cliente, ClienteDAO
from models.categoria import Categoria, CategoriaDAO
from models.produto import Produto, ProdutoDAO
from models.compra import Compra, CompraDAO

class View:
    # ======== Clientes ========
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(c)
        print(f"✅ Cliente {nome} inserido com sucesso!")

    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_listar_id(id_cliente):
        return ClienteDAO.listar_id(id_cliente)

    @staticmethod
    def cliente_atualizar(id_cliente, nome, email, fone, senha):
        c = Cliente(id_cliente, nome, email, fone, senha)
        ClienteDAO.atualizar(c)
        print(f"✅ Cliente {id_cliente} atualizado!")

    @staticmethod
    def cliente_excluir(id_cliente):
        c = Cliente(id_cliente, "", "", "", "")
        ClienteDAO.excluir(c)
        print(f"✅ Cliente {id_cliente} excluído!")

    # ======== Categorias ========
    @staticmethod
    def categoria_inserir(descricao):
        c = Categoria(0, descricao)
        CategoriaDAO.inserir(c)
        print(f"✅ Categoria '{descricao}' inserida!")

    @staticmethod
    def categoria_listar():
        return CategoriaDAO.listar()

    @staticmethod
    def categoria_listar_id(id_categoria):
        return CategoriaDAO.listar_id(id_categoria)

    @staticmethod
    def categoria_atualizar(id_categoria, descricao):
        c = Categoria(id_categoria, descricao)
        CategoriaDAO.atualizar(c)
        print(f"✅ Categoria {id_categoria} atualizada!")

    @staticmethod
    def categoria_excluir(id_categoria):
        c = Categoria(id_categoria, "")
        CategoriaDAO.excluir(c)
        print(f"✅ Categoria {id_categoria} excluída!")

class ItemCarrinho:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def get_total(self):
        return self.produto.get_preco() * self.quantidade

class View:

    def listar_produtos():
        produtos = ProdutoDAO.listar()
        if not produtos:
            print("Nenhum produto disponível.")
            return []
        print("\n=== PRODUTOS DISPONÍVEIS ===")
        for p in produtos:
            print(f"ID: {p.get_id()} | {p.get_descricao()} | Preço: R${p.get_preco():.2f} | Estoque: {p.get_estoque()}")
        return produtos

    def inserir_produto_carrinho(id_cliente, id_produto, quantidade):
        cliente = ClienteDAO.listar_id(id_cliente)
        produto = ProdutoDAO.listar_id(id_produto)
        if not cliente or not produto:
            print("❌ Cliente ou produto inválido.")
            return
        if produto.get_estoque() < quantidade:
            print("❌ Estoque insuficiente.")
            return
        if not hasattr(cliente, "carrinho"):
            cliente.carrinho = []
        for item in cliente.carrinho:
            if item.produto.get_id() == id_produto:
                item.quantidade += quantidade
                print(f"✅ Quantidade de {produto.get_descricao()} atualizada no carrinho.")
                return
        cliente.carrinho.append(ItemCarrinho(produto, quantidade))
        print(f"✅ {produto.get_descricao()} adicionado ao carrinho.")

    def visualizar_carrinho(id_cliente):
        cliente = ClienteDAO.listar_id(id_cliente)
        if not cliente or not hasattr(cliente, "carrinho") or not cliente.carrinho:
            print("🛒 Carrinho vazio.")
            return []
        total = 0
        print(f"\n=== CARRINHO DE {cliente.get_nome()} ===")
        for item in cliente.carrinho:
            subtotal = item.get_total()
            total += subtotal
            print(f"{item.produto.get_descricao()} | Qtd: {item.quantidade} | Total: R${subtotal:.2f}")
        print(f"Total do carrinho: R${total:.2f}")
        return cliente.carrinho

    def comprar_carrinho(id_cliente):
        cliente = ClienteDAO.listar_id(id_cliente)
        if not cliente or not hasattr(cliente, "carrinho") or not cliente.carrinho:
            print("❌ Carrinho vazio.")
            return
        total_compra = 0
        for item in cliente.carrinho:
            produto = item.produto
            if produto.get_estoque() < item.quantidade:
                print(f"❌ Estoque insuficiente para {produto.get_descricao()}. Compra cancelada.")
                return
            produto.set_estoque(produto.get_estoque() - item.quantidade)
            ProdutoDAO.atualizar(produto)
            total_compra += item.get_total()
        compra = Compra(id_cliente, cliente.carrinho.copy())
        CompraDAO.inserir(compra)
        if not hasattr(cliente, "compras"):
            cliente.compras = []
        cliente.compras.append(compra)
        cliente.carrinho.clear()
        print(f"💰 Compra realizada com sucesso! Total: R${total_compra:.2f}")

    def listar_minhas_compras(id_cliente):
        compras = CompraDAO.listar_por_cliente(id_cliente)
        if not compras:
            print("Nenhuma compra encontrada.")
            return
        print(f"\n=== COMPRAS DO CLIENTE {id_cliente} ===")
        for c in compras:
            print(c)

    def listar_vendas_admin():
        vendas = CompraDAO.listar()
        if not vendas:
            print("Nenhuma venda registrada.")
            return
        print("\n=== TODAS AS VENDAS ===")
        for c in vendas:
            print(c)