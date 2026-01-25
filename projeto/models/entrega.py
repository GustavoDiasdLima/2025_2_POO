import json
from models.dao import DAO

class Entrega:
    def __init__(self, id, id_venda, endereco, status, previsao):
        self.__id = id
        self.__id_venda = id_venda
        self.__endereco = endereco
        self.__status = status      # Ex: "Em preparo", "Enviado", "Entregue"
        self.__previsao = previsao  # Ex: "25/06/2026"

    def get_id_venda(self): return self.__id_venda
    def get_status(self): return self.__status
    def get_previsao(self): return self.__previsao
    def get_endereco(self): return self.__endereco
class EntregaDAO(DAO):
    objetos = []

    @classmethod
    def abrir(cls):
        if not hasattr(cls, "objetos"):
            cls.objetos = []

    @classmethod
    def inserir(cls, entrega):
        cls.abrir()
        cls.objetos.append(entrega)
        cls.salvar()  # se tiver implementado

    @classmethod
    def listar_por_venda(cls, id_venda):
        cls.abrir()
        for e in cls.objetos:
            if e.get_id_venda() == id_venda:
                return e
        return None

