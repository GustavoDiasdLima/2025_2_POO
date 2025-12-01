from projeto import Cliente, ClienteDAO
from projeto import Categoria, CategoriaDAO
from projeto import Produto, ProdutoDAO
from projeto import Venda,VendaDAO
from projeto import Carrinho, CarrinhoDAO

class View:

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

    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(c)
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(c)
    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(c)

    def categoria_inserir(descricao):
        c = Categoria(0, descricao)
        CategoriaDAO.inserir(c)
    def categoria_listar():
        return CategoriaDAO.listar()
    def categoria_listar_id(id):
        return CategoriaDAO.listar_id(id)
    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)
    def categoria_excluir(id):
        c = Categoria(id, "")
        CategoriaDAO.excluir(c)

    def produto_inserir(descricao, preco, estoque, id_categoria):
        c = Produto(0, descricao, preco, estoque, id_categoria)
        ProdutoDAO.inserir(c)
    def produto_listar():
        return ProdutoDAO.listar()
    def produto_listar_id(id):
        return ProdutoDAO.listar_id(id)
    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        c = Produto(id, descricao, preco, estoque, id_categoria)
        ProdutoDAO.atualizar(c)
    def produto_excluir(id):
        c = Produto(id, "", 0, 0, 0)
        ProdutoDAO.excluir(c)
    def produto_reajustar(percentual):
        for obj in ProdutoDAO.listar():
            obj.reajustar()
            #obj.preco = obj.preco * (1 + percentual)
            ProdutoDAO.atualizar(obj)
    def carrinho_inserir(id_cliente, id_produto):
        c = Carrinho(0, id_cliente, id_produto)
        CarrinhoDAO.inserir(c)
    def carrinho_listar(id_cliente):
        return CarrinhoDAO.listar_por_cliente(id_cliente)
    def carrinho_comprar(id_cliente):
        # o DAO faz a compra: cria vendas, limpa carrinho etc.
        return CarrinhoDAO.comprar(id_cliente)
    def venda_listar(id_cliente):
        return VendaDAO.listar_por_cliente(id_cliente)
    def venda_listar_todas():
        return VendaDAO.listar()
    @classmethod
    def listar_vendas_admin(cls):
        print("Todas as vendas:")
        vendas = View.venda_listar_todas()
        if len(vendas) == 0:
            print("Nenhuma venda registrada.")
        else:
            for v in vendas:
                print(v)