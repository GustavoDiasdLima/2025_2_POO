class Compra:
    _id_auto = 1
    def __init__(self, id_cliente, itens):
        self.id = Compra._id_auto
        Compra._id_auto += 1
        self.id_cliente = id_cliente
        self.itens = itens  # lista de ItemCarrinho
        self.total = sum(i.get_total() for i in itens)

    def __str__(self):
        texto = f"Compra {self.id} | Cliente {self.id_cliente} | Total R${self.total:.2f}"
        for i in self.itens:
            texto += f"\n - {i.produto.get_descricao()} x{i.quantidade} = R${i.get_total():.2f}"

class CompraDAO(DAO):
    _compras = []

    @staticmethod
    def inserir(compra):
        CompraDAO._compras.append(compra)

    @staticmethod
    def listar():
        return CompraDAO._compras

    @staticmethod
    def listar_por_cliente(id_cliente):
        return [c for c in CompraDAO._compras if c.id_cliente == id_cliente]