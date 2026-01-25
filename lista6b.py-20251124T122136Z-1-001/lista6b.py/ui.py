from models.cliente import Cliente, ClienteDAO
from models.categoria import Categoria, CategoriaDAO
from models.venda import Venda, VendaDAO
from views import View

class UI: # classe estática -> não tem instância
    __usuario = None     

    def menu_visitante():
        print("1-Entrar no Sistema, 2-Abrir Conta, 9-Fim")
        op = int(input("Informe uma opção: "))           
        if op == 1: UI.visitante_entrar()
        if op == 2: UI.visitante_criar_conta()
        return op

    def menu_admin():
        print("Clientes   : 1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print("Categorias : 5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print("Produtos   : 9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir")
        print("13-Listar Vendas, 14-Sair")
        op = int(input("Informe uma opção: "))           
        if op == 1: UI.cliente_inserir()
        if op == 2: UI.cliente_listar()
        if op == 3: UI.cliente_atualizar()
        if op == 4: UI.cliente_excluir()
        if op == 5: UI.categoria_inserir()
        if op == 6: UI.categoria_listar()
        if op == 7: UI.categoria_atualizar()
        if op == 8: UI.categoria_excluir()
        if op == 9: UI.produto_inserir()
        if op == 10: UI.produto_listar()
        if op == 11: UI.produto_atualizar()
        if op == 12: UI.produto_excluir()
        if op == 13: UI.listar_vendas_admin()
        if op == 14: UI.usuario_sair()

    def menu_cliente():
        print("1-Listar produtos")
        print("2-Inserir produto no carrinho")
        print("3-Visualizar carrinho")
        print("4-Comprar carrinho")
        print("5-Indisponível :()")
        print("9-Sair")
        op = int(input("Informe uma opção: "))           
        if op == 1: UI.listar_produtos()
        if op == 2: UI.inserir_produto_carrinho()
        if op == 3: UI.visualizar_carrinho()
        if op == 4: UI.comprar_carrinho()
        if op == 5: pass
        if op == 9: UI.usuario_sair()

    @classmethod
    def main(cls):
        # verifica a existe o usuário admin
        View.cliente_criar_admin()
        # mostra o menu da aplicação
        UI.menu()
        
    @classmethod
    def menu(cls):
        op = 0
        while op != 9:
            if cls.__usuario == None: 
                # usuário não está logado
                op = UI.menu_visitante()
            else:
                # usuário está logado, verifica se é o admin
                admin = cls.__usuario["nome"] == "admin"
                # mensagem de bem-vindo
                print("IF Comércio Eletrônico 2025")
                print("Bem-vindo(a), " + cls.__usuario["nome"])
                # menu do usuário: admin ou cliente
                if admin: UI.menu_admin()
                else: UI.menu_cliente()

    @classmethod
    def visitante_entrar(cls):
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        cls.__usuario = View.cliente_autenticar(email, senha)
        if cls.__usuario == None: print("Usuário ou senha inválidos")

    def visitante_criar_conta():
        UI.cliente_inserir()

    @classmethod
    def usuario_sair(cls):
        cls.__usuario = None

    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        senha = input("Informe a senha: ")
        View.cliente_inserir(nome, email, fone, senha)

    def cliente_listar():
        for obj in View.cliente_listar(): print(obj)       

    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        senha = input("Informe a nova senha: ")
        View.cliente_atualizar(id, nome, email, fone, senha)

    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.cliente_excluir(id)

    def categoria_inserir():
        descricao = input("Informe a descrição: ")
        View.categoria_inserir(descricao)

    def categoria_listar():
        for obj in View.categoria_listar(): print(obj)      

    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe a categoria a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        View.categoria_atualizar(id, descricao)

    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.categoria_excluir(id)
    
    #peodutos
    def produto_inserir():
        descricao = input("Informe o produto: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe a quantidade: "))
        id_categoria = input("Informe o id: ")
        View.produto_inserir(descricao, preco, estoque, id_categoria)

    def produto_listar():
        for obj in View.produto_listar(): print(obj)      

    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o produto a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        preco = input("Informe o preço: ")
        estoque = input("Informe a quantidade: ")
        id_categoria = input("Informe o id: ")
        View.produto_atualizar(id, descricao, estoque, id_categoria, preco)

    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o produto a ser excluído: "))
        View.produto_excluir(id)
    
    @classmethod
    def listar_vendas_admin(cls):
        print("Lista de todas as vendas:")
        for obj in View.venda_listar_todas():
            print(obj)

    @classmethod
    def listar_produtos(cls):
        print("Lista de produtos:")
        for obj in View.produto_listar():
            print(obj)
         
    @classmethod     
    def inserir_produto_carrinho(cls):
        if cls.__usuario is None:
            print("Você precisa estar logado.")
            return
        
        UI.listar_produtos()
        id_prod = int(input("Informe o id do produto para adicionar ao carrinho: "))
        View.carrinho_inserir(cls.__usuario["id"], id_prod)
        print("Produto inserido no carrinho.")

    @classmethod  
    def visualizar_carrinho(cls):
        if cls.__usuario is None:
            print("Você precisa estar logado.")
            return
        print("Seu carrinho:")
        lista = View.carrinho_listar(id_cliente)
        if len(lista) == 0:
            print("Carrinho vazio.")
        else:
            for item in lista:
                print(item)

    @classmethod   
    def comprar_carrinho(cls):
        if cls.__usuario is None:
            print("Você precisa estar logado.")
            return
        ok = View.carrinho_comprar(cls.__usuario["id"])
        if ok:
            print("Compra realizada com sucesso!")
        else:
            print("Seu carrinho está vazio.")
    @classmethod
    def listar_vendas(cls):
        if cls.__usuario is None:
            print("Você precisa estar logado.")
            return
        
        print("Minhas compras:")
        vendas = View.venda_listar(cls.__usuario["id"])
        if len(vendas) == 0:
            print("Nenhuma compra encontrada.")
        else:
            for v in vendas:
                print(v)
UI.main()