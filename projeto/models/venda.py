import json

class Venda:
    def __init__(self, id, data, carrinho, itens, total, id_venda, id_cliente):
        self.id = id          
        self.data = data
        self.itens = itens    
        self.carrinho = carrinho      
        self.total = total  
        self.id_venda = id_venda    
        self.id_cliente = id_cliente      


    def __str__(self):
        return f"{self.id} - {self.data} - {self.carrinho} - {self.total}" 

    def get_id(self): return self.id
    def get_data(self): return self.data
    def get_carrinho(self): return self.carrinho
    def get_total(self): return self.total
    def get_id_cliente(self): return self.id_cliente

    def set_id(self, id): self.id = id
    def set_data(self, data): self.data = data
    def set_carrinho(self, carrinho): self.carrinho = carrinho
    def set_total(self, total): self.total = total
    def set_id_cliente(self, id_cliente): self.id_cliente = id_cliente

    def to_json(self):
        return { "id" : self.id, "data" : self.data, "carrinho" : self.carrinho, "total" : self.total, "id_cliente" : self.id_cliente }

    @staticmethod
    def from_json(dic):
        return Venda(dic["id"], dic["data"], dic["carrinho"], dic["total"], dic["id_cliente"])


class VendaDAO:               # classe estática -> não tem instância
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
    def listar_por_cliente(cls, id_cliente):
        cls.abrir()
        lista = []
        for v in cls.objetos:
            if v.get_id_cliente() == id_cliente:
                lista.append(v)
        return lista
    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Venda.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Venda.from_json(dic)
                    cls.objetos.append(c)
                    
        except:
            pass            