import json
from models.dao import DAO


class Feedback:
    def __init__(self, id, nota, comentario, data, id_cliente):
        self.set_id(id)
        self.set_nota(nota)
        self.set_comentario(comentario)
        self.set_data(data)
        self.set_id_cliente(id_cliente)
    

    def get_id(self): return self.__id
    def get_nota(self): return self.__nota
    def get_comentario(self): return self.__comentario
    def get_data(self): return self.__data
    def get_id_cliente(self): return self.__id_cliente
   
    def set_id(self, id): self.__id = id
    def set_nota(self, nota): self.__nota = nota
    def set_comentario(self, comentario): self.__comentario = comentario
    def set_data(self, data): self.__data = data
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
   

    def to_json(self):
        return {
            "id": self.__id,
            "nota": self.__nota,
            "comentario": self.__comentario,
            "data": self.__data,
            "id_cliente": self.__id_cliente
        }

    @staticmethod
    def from_json(dic):
        return Feedback(
            dic["id"],
            dic["nota"],
            dic["comentario"],
            dic["data"],
            dic["id_cliente"]
        )


class FeedbackDAO(DAO):
    @classmethod
    def proximo_id(cls):
        cls.abrir()  # garante que objetos estão carregados
        if not cls.objetos:
            return 1
        else:
            # pega o maior id atual + 1
            return max(f.get_id() for f in cls.objetos) + 1

    @classmethod
    def inserir(cls, feedback):
        cls.abrir()  # garante que objetos estão carregados
        cls.objetos.append(feedback)
        cls.salvar()

    @classmethod
    def salvar(cls):
        with open("feedbacks.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=Feedback.to_json, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("feedbacks.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    cls.objetos.append(Feedback.from_json(dic))
        except:
            pass

