class ClienteDAO:
    _clientes = []
    _id_auto = 1

    @staticmethod
    def inserir(c):
        c.id = ClienteDAO._id_auto
        ClienteDAO._id_auto += 1
        ClienteDAO._clientes.append(c)

    @staticmethod
    def listar():
        return ClienteDAO._clientes

    @staticmethod
    def listar_id(id):
        for c in ClienteDAO._clientes:
            if c.get_id() == id:
                return c
        return None

    @staticmethod
    def atualizar(c):
        for i, cli in enumerate(ClienteDAO._clientes):
            if cli.get_id() == c.get_id():
                ClienteDAO._clientes[i] = c

    @staticmethod
    def excluir(c):
        ClienteDAO._clientes = [cli for cli in ClienteDAO._clientes if cli.get_id() != c.get_id()]
