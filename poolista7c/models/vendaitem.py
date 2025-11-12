import json

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


class VendaItemDAO:           # classe estática -> não tem instância
    objetos = []              # atributo da classe
    @classmethod              # classe DAO não vai ter instância
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
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
            if obj.get_id() == id: return obj
        return None    
    @classmethod
    def atualizar(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            # remove o objeto antigo aux e insere o novo obj
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("vendaitens.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = VendaItem.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendaitens.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = VendaItem.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            