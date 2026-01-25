import json
from models.dao import DAO
from datetime import date, datetime

class Promocao:
    def __init__(self, id, titulo, descricao, desconto, data_inicio, data_fim):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_descricao(descricao)
        self.set_desconto(desconto)
        self.set_data_inicio(data_inicio)
        self.set_data_fim(data_fim)

  
    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_descricao(self): return self.__descricao
    def get_desconto(self): return self.__desconto
    def get_data_inicio(self): return self.__data_inicio
    def get_data_fim(self): return self.__data_fim

   
    def set_id(self, id): self.__id = id
    def set_titulo(self, titulo): self.__titulo = titulo
    def set_descricao(self, descricao): self.__descricao = descricao
    def set_desconto(self, desconto): self.__desconto = desconto
    def set_data_inicio(self, data_inicio): self.__data_inicio = data_inicio
    def set_data_fim(self, data_fim): self.__data_fim = data_fim

    def to_json(self):
        return {
            "id": self.__id,
            "titulo": self.__titulo,
            "descricao": self.__descricao,
            "desconto": self.__desconto,
            "data_inicio": self.__data_inicio,
            "data_fim": self.__data_fim
        }

    @staticmethod
    def from_json(dic):
        return Promocao(
            dic["id"],
            dic["titulo"],
            dic["descricao"],
            dic["desconto"],
            dic["data_inicio"],
            dic["data_fim"]
        )

class PromocaoDAO(DAO):
    @classmethod
    def proximo_id(cls):
        cls.abrir()
        if not hasattr(cls, "objetos") or not cls.objetos:
            return 1
        return max(p.get_id() for p in cls.objetos) + 1

    @classmethod
    def inserir(cls, promocao):
        cls.abrir()
        cls.objetos.append(promocao)
        cls.salvar()

    @classmethod
    def salvar(cls):
        with open("promocoes.json", "w") as f:
            json.dump(cls.objetos, f, default=Promocao.to_json, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("promocoes.json", "r") as f:
                lista = json.load(f)
                for dic in lista:
                    cls.objetos.append(Promocao.from_json(dic))
        except:
            pass

    @classmethod
    def listar_ativas(cls):
        cls.abrir()
        hoje = datetime.now().date()  # data atual
        ativas = []
        for p in cls.objetos:
            # converte strings para date
            inicio = datetime.strptime(p.get_data_inicio(), "%Y-%m-%d").date()
            fim = datetime.strptime(p.get_data_fim(), "%Y-%m-%d").date()
            if inicio <= hoje <= fim:
                ativas.append(p)
        return ativas

