import json
class VendaItem:
    def __init__(self, id, qtd, preco, idVenda, idProduto):
        self.id = id
        self.qtd = qtd
        self.preco = preco
        self.idVenda = idVenda
        self.idProduto
    def __str__(self):
        return f"{self.id} - {self.qtd} - {self.preco} - {self.idVenda} - {self.idProduto}"
    
class ProdutoDAO:             # classe estática -> não tem instância
    objetos = []              # atributo da classe
    @classmethod              # classe DAO não vai ter instância
    def inserir(cls, obj):  #MÉTODO inserir
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.id > id: id = aux.id
        obj.id = id + 1    
        cls.objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):  #método para listar
        cls.abrir()
        return cls.objetos
    @classmethod
    def listar_id(cls, id): #método listar id
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id: return obj
        return None    
    @classmethod
    def atualizar(cls, obj): #método atualizar
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.id)
        if aux != None:
            #aux.nome = obj.nome
            # remove o objeto antigo aux e insere o novo obj
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):  #método excluir
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.id)
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls): #método salvar
        with open("VendaItem.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars, indent=4)
    @classmethod
    def abrir(cls):  #método abrir
        cls.objetos = []
        try:
            with open("VendaItem.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = VendaItem(dic["id"], dic["nome"])
                    cls.objetos.append(c)
        except:
            pass            