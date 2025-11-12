#from models.cliente import Cliente, ClienteDAO
#from models.categoria import Categoria, CategoriaDAO
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
        print("9-Sair")
        op = int(input("Informe uma opção: "))           
        if op == 1: UI.cliente_inserir()
        if op == 2: UI.cliente_listar()
        if op == 3: UI.cliente_atualizar()
        if op == 4: UI.cliente_excluir()
        if op == 5: UI.categoria_inserir()
        if op == 6: UI.categoria_listar()
        if op == 7: UI.categoria_atualizar()
        if op == 8: UI.categoria_excluir()
        if op == 9: UI.usuario_sair()

    def menu_cliente():
        print("1-Listar produtos")
        print("2-Inserir produto no carrinho")
        print("3-Visualizar carrinho")
        print("4-Comprar carrinho")
        print("5-Listar minhas compras")
        print("9-Sair")
        op = int(input("Informe uma opção: "))           
        if op == 1: pass
        if op == 2: pass
        if op == 3: pass
        if op == 4: pass
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
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        View.categoria_atualizar(id, descricao)

    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id a ser excluído: "))
        View.categoria_excluir(id)

UI.main()