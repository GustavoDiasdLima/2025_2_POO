import json
from datetime import datetime
from models.venda import Venda, VendaDAO
from models.produto import ProdutoDAO


class Carrinho:
    def __init__(self, id, id_cliente, id_produto):
        self.set_id(id)
        self.set_id_cliente(id_cliente)
        self.set_id_produto(id_produto)

    def __str__(self):
        return f"{self.__id} - Cliente {self.__id_cliente} - Produto {self.__id_produto}"

    # Getters
    def get_id(self): return self.__id
    def get_id_cliente(self): return self.__id_cliente
    def get_id_produto(self): return self.__id_produto

    # Setters
    def set_id(self, id): self.__id = id
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_produto(self, id_produto): self.__id_produto = id_produto

    def to_json(self):
        return {
            "id": self.__id,
            "id_cliente": self.__id_cliente,
            "id_produto": self.__id_produto
        }

    @staticmethod
    def from_json(dic):
        return Carrinho(dic["id"], dic["id_cliente"], dic["id_produto"])


class CarrinhoDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        novo_id = 0
        for aux in cls.objetos:
            if aux.get_id() > novo_id:
                novo_id = aux.get_id()
        obj.set_id(novo_id + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None


    @classmethod
    def listar_por_cliente(cls, id_cliente):
        cls.abrir()
        lista = []
        for obj in cls.objetos:
            if obj.get_id_cliente() == id_cliente:
                lista.append(obj)
        return lista

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.objetos.remove(aux)
            cls.salvar()

    @classmethod
    def comprar(cls, id_cliente):
        cls.abrir()
        itens = cls.listar_por_cliente(id_cliente)

        if len(itens) == 0:
            return False  # carrinho vazio

        total = 0
        lista_produtos = []

        for item in itens:
            prod = ProdutoDAO.listar_id(item.get_id_produto())
            if prod is not None:
                total += prod.get_preco()
                lista_produtos.append(prod.get_descricao())

        venda = Venda(
            0,
            datetime.now().strftime("%d/%m/%Y %H:%M"),
            lista_produtos,
            total,
            id_cliente
        )

        VendaDAO.inserir(venda)

        # limpar carrinho do cliente
        for item in itens:
            cls.objetos.remove(item)
        cls.salvar()

        return True

    @classmethod
    def salvar(cls):
        with open("carrinhos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo,
                      default=Carrinho.to_json, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("carrinhos.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    obj = Carrinho.from_json(dic)
                    cls.objetos.append(obj)
        except:
            pass