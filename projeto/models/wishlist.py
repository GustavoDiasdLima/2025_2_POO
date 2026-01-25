# models/wishlist.py
import json
from models.dao import DAO
from models.produto import ProdutoDAO

class Wishlist:
    def __init__(self, id, id_cliente, id_produto):
        self.set_id(id)
        self.set_id_cliente(id_cliente)
        self.set_id_produto(id_produto)

   
    def get_id(self): return self.__id
    def get_id_cliente(self): return self.__id_cliente
    def get_id_produto(self): return self.__id_produto

 
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
        return Wishlist(dic["id"], dic["id_cliente"], dic["id_produto"])

class WishlistDAO(DAO):

    @classmethod
    def listar_por_cliente(cls, id_cliente):
        cls.abrir()
        return [w for w in cls.objetos if w.get_id_cliente() == id_cliente]

    @classmethod
    def inserir(cls, wishlist):
        cls.abrir()
        cls.objetos.append(wishlist)
        cls.salvar()

    @classmethod
    def remover(cls, id_cliente, id_produto):
        cls.abrir()
        cls.objetos = [w for w in cls.objetos if not (w.get_id_cliente()==id_cliente and w.get_id_produto()==id_produto)]
        cls.salvar()

    @classmethod
    def salvar(cls):
        with open("wishlist.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=Wishlist.to_json, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("wishlist.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    cls.objetos.append(Wishlist.from_json(dic))
        except:
            pass
