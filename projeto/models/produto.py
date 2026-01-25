import json
from models.dao import DAO



class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.set_id(id)          
        self.set_descricao(descricao)      
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_id_categoria(id_categoria)

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__preco} - {self.__estoque}" 

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_preco(self): return self.__preco
    def get_estoque(self): return self.__estoque
    def get_id_categoria(self): return self.__id_categoria

    def set_id(self, id): self.__id = id
    def set_descricao(self, descricao): self.__descricao = descricao
    def set_preco(self, preco): self.__preco = float(preco)
    def set_estoque(self, estoque): self.__estoque = estoque
    def set_id_categoria(self, id_categoria): self.__id_categoria = id_categoria

    def to_json(self):
        return { "id" : self.__id, "descricao" : self.__descricao, "preco" : self.__preco, "estoque" : self.__estoque, "id_categoria" : self.__id_categoria } 

    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], float(dic["preco"]), int(dic["estoque"]), dic["id_categoria"])

    def reajustar(self, percentual): self.__preco * (1 + percentual/100)


class ProdutoDAO(DAO):             # classe estática -> não tem instância

    @classmethod
    def listar_id(cls, id_produto):
        cls.abrir()
        for p in cls.objetos:
            if p.get_id() == id_produto:
                return p
        return None

    @classmethod
    def listar_descricao(cls, descricao):
        cls.abrir()
        for p in cls.objetos:
            if p.get_descricao() == descricao:
                return p
        return None

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Produto.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Produto.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            