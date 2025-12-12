import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)          # atributo de instância
        self.set_nome(nome)      # cada cliente (instância) tem id e nome
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha

    def set_id(self, id): self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_fone(self, fone): self.__fone = fone
    def set_senha(self, senha): self.__senha = senha

    def to_json(self):
        return { "id" : self.__id, "nome" : self.__nome, "email" : self.__email, "fone" : self.__fone, "senha" : self.__senha }

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])


class ClienteDAO:             # classe estática -> não tem instância
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
    def excluir(cls, id):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(id)
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Cliente.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Cliente.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            