from abc import ABC

class DAO(ABC):

    objetos = []                           
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def lista_id(cls, id):
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        aux = cls.lista_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        aux = cls.lista_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def proximo_id(cls):
        cls.abrir()
        if len(cls.objetos) == 0:
            return 1
        return max(obj.get_id() for obj in cls.objetos) + 1

    @classmethod
    def salvar(cls):
        pass
    @classmethod
    def abrir(cls):
        pass