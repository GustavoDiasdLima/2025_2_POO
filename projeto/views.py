from models.cliente import Cliente
from models.cliente import ClienteDAO
from models.categoria import Categoria, CategoriaDAO
from models.produto import Produto, ProdutoDAO
from models.venda import Venda, VendaDAO
from models.vendaitem import VendaItemDAO
from models.carrinho import Carrinho, CarrinhoDAO
from models.promocao import Promocao, PromocaoDAO
from models.entrega import EntregaDAO
from models.feedback import FeedbackDAO
from models.wishlist import WishlistDAO

from models.dao import DAO

class View:

    @staticmethod
    def cliente_criar_admin():
        # cria o usuário admin se ele não existir
        for obj in View.cliente_listar():
            if obj.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234") 


    def cliente_autenticar(email, senha):
        for obj in View.cliente_listar():
            if obj.get_email() == email and obj.get_senha() == senha: 
                return { "id": obj.get_id(), "nome": obj.get_nome() }
        return None

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        for obj in View.cliente_listar():
            if obj.get_email() == email:
                raise ValueError("E-mail repetido")
        c = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(c)
        return c   
    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(c)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO.excluir(id)
    @staticmethod
    def categoria_inserir(descricao):
        c = Categoria(0, descricao)
        CategoriaDAO.inserir(c)
    @staticmethod
    def categoria_listar():
        return CategoriaDAO.listar()
    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO.listar_id(id)
    @staticmethod
    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)
    @staticmethod
    def categoria_excluir(id):
        c = Categoria(id, "")
        CategoriaDAO.excluir(c)
    @staticmethod
    def produto_inserir(descricao, preco, estoque, id_categoria):
        c = Produto(0, descricao, preco, estoque, id_categoria)
        ProdutoDAO.inserir(c)
    @staticmethod
    def produto_listar():
        return ProdutoDAO.listar()
    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO.listar_id(id)
    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        c = Produto(id, descricao, preco, estoque, id_categoria)
        ProdutoDAO.atualizar(c)
    @staticmethod
    def produto_excluir(id):
        c = Produto(id, "", 0, 0, 0)
        ProdutoDAO.excluir(c)
    @staticmethod
    def produto_reajustar(percentual):
        for obj in ProdutoDAO.listar():
            obj.reajustar()
            #obj.preco = obj.preco * (1 + percentual)
            ProdutoDAO.atualizar(obj)
    @staticmethod
    def carrinho_inserir(id_cliente, id_produto):
        c = Carrinho(0, id_cliente, id_produto)
        CarrinhoDAO.inserir(c)
    @staticmethod
    def carrinho_listar(id_cliente):
        return CarrinhoDAO.listar_por_cliente(id_cliente)
    @staticmethod
    def carrinho_comprar(id_cliente):
        # o DAO faz a compra: cria vendas, limpa carrinho etc.
        return CarrinhoDAO.comprar(id_cliente)
    @staticmethod
    def venda_listar(id_cliente):
        return VendaDAO.listar_por_cliente(id_cliente)
    @staticmethod
    def venda_listar_todas():
        return VendaDAO.listar()
    @staticmethod
    def vendaitem_listar_por_venda(id_venda):
        return VendaItemDAO.listar_por_venda(id_venda)
    @classmethod
    def listar_vendas_admin(cls):
        print("Todas as vendas:")
        vendas = View.venda_listar_todas()
        if len(vendas) == 0:
            print("Nenhuma venda registrada.")
        else:
            for v in vendas:
                print(v)
    def reajustar(percentual):
        for obj in ProdutoDAO.listar():
            obj.reajustar(percentual)
    @staticmethod
    def promocao_criar(id_produto, desconto):
        p = Promocao(
            PromocaoDAO.proximo_id(),
            id_produto,
            desconto,
            True
        )
        PromocaoDAO.inserir(p)

    @staticmethod
    def promocao_buscar_por_produto(id_produto):
        return PromocaoDAO.buscar_por_produto(id_produto)
            
    @staticmethod
    def entrega_buscar_por_venda(id_venda):
        return EntregaDAO.listar_por_venda(id_venda)
    
    @staticmethod
    def feedback_listar_por_produto(id_produto):
        return FeedbackDAO.listar_por_produto(id_produto)
    @staticmethod
    def wishlist_listar(id_cliente):
        return WishlistDAO.listar_por_cliente(id_cliente)
        