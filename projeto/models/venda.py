import json
from models.dao import DAO


class Venda:
    def __init__(self, id, data, total, id_cliente):
        self.__id = id
        self.__data = data
        self.__total = total
        self.__id_cliente = id_cliente

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_total(self): return self.__total
    def get_id_cliente(self): return self.__id_cliente

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data,
            "total": self.__total,
            "id_cliente": self.__id_cliente
        }

    @staticmethod
    def from_json(dic):
        return Venda(
            dic["id"],
            dic["data"],
            dic["total"],
            dic["id_cliente"]
        )

class VendaDAO(DAO):

    @classmethod
    def listar_por_cliente(cls, id_cliente):
        cls.abrir()
        return [v for v in cls.objetos if v.get_id_cliente() == id_cliente]

    @classmethod
    def salvar(cls):
        with open("vendas.json", "w") as f:
            json.dump(cls.objetos, f, default=Venda.to_json, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendas.json", "r") as f:
                for dic in json.load(f):
                    cls.objetos.append(Venda.from_json(dic))
        except:
            pass
