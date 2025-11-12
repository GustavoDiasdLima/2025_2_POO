from models.cliente import Cliente, ClienteDAO
from models.categoria import Categoria, CategoriaDAO
from models.produto import Produto, ProdutoDAO

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
        
    def carrinho_inserir(id, nome, preco, quantidade):

    def carrinho_listas(id, nome, quantidade):

    def carrinho_visualizar(quantidade, nome):

    def carrinho_comprar(id, preco, quantidade):

    def listas_minhas_compras(preco, quantidade, id):