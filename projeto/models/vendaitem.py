import json
from models.dao import DAO

class VendaItem:
    def __init__(self, id, qtd, preco, id_venda, id_produto):
        self.set_id(id)          
        self.set_qtd(qtd)      
        self.set_preco(preco)
        self.set_id_venda(id_venda)
        self.set_id_produto(id_produto)

    def __str__(self):
        return f"{self.__id} - {self.__qtd} - {self.__preco:.2f}" 

    def get_id(self): return self.__id
    def get_qtd(self): return self.__qtd
    def get_preco(self): return self.__preco
    def get_id_venda(self): return self.__id_venda
    def get_id_produto(self): return self.__id_produto

    def set_id(self, id): self.__id = id
    def set_qtd(self, qtd): self.__qtd = qtd
    def set_preco(self, preco): self.__preco = preco
    def set_id_venda(self, id_venda): self.__id_venda = id_venda
    def set_id_produto(self, id_produto): self.__id_produto = id_produto

    def to_json(self):
        return { "id" : self.__id, "qtd" : self.__qtd, "preco" : self.__preco, "id_venda" : self.__id_venda, "id_produto" : self.__id_produto }

    @staticmethod
    def from_json(dic):
        return VendaItem(dic["id"], dic["qtd"], dic["preco"], dic["id_venda"], dic["id_produto"])


class VendaItemDAO(DAO):

    @classmethod
    def listar_por_venda(cls, id_venda):
        cls.abrir()
        return [i for i in cls.objetos if i.get_id_venda() == id_venda]

    @classmethod
    def salvar(cls):
        with open("vendaitens.json", "w") as f:
            json.dump(cls.objetos, f, default=VendaItem.to_json, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendaitens.json", "r") as f:
                for dic in json.load(f):
                    cls.objetos.append(VendaItem.from_json(dic))
        except:
            pass
