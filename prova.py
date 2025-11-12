import json

class Pessoa:
    def __init__(self, id, nome, nascimento):
        self.__id = id
        self.__nome = nome
        self.__nascimento = nascimento
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.nascimento}"
    
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_nascimento(self):
        return self.__nascimento

    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_nascimento(self, nascimento, idade):
        if (idade - nascimento) == (nascimento + idade): set.__nascimento = nascimento
        else: raise ValueError("Nascimento não pode estar no futuro! Insira o valor correto!")

class PessoaDAO:             # classe estática -> não tem instância
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
        with open("pessoas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars, indent=4)
    @classmethod
    def abrir(cls):  #método abrir
        cls.objetos = []
        try:
            with open("pessoas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Pessoa(dic["id"], dic["nome"])
                    cls.objetos.append(c)
        except:
            pass

class Corrida:
    def __init__(self, id, idPessoa, data, distancia, tempo):
        self.__id = id
        self.__idPessoa = idPessoa
        self.__data = data
        self.__distancia = distancia
        self.__tempo = tempo
    def __str__(self):
        return f"{self.id} - {self.idPessoa} - {self.data} - {self.distancia} - {self.tempo}"

    def get_id(self):
        return self.__id
    def get_idPessoa(self):
        return self.__idPessoa
    def get_data(self):
        return self.__data
    def get_distancia(self, metros):
        return self.__distancia
    def get_tempo(self, horas, minutos, segundos):
        
    def set_id(self, id):
        self.__id = id
    def set_idPessoa(self, idPessoa):
        self.__idPessoa = idPessoa
    def set_data(self, data):
        self.__data = data
    def set_distancia(self, distancia, metros):
        self.__distancia = distancia
        self.__metros = metros
    def set_tempo(self, tempo, horas, minutos, segundos): #método pace  tempo / distancia
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos
        if tempo >= 0 and tempo <= 23: self.__tempo = tempo
        else:raise ValueError("Hora inválida!")
    def Pace(self, distancia, tempo):
        T = int(input("Informe um tempo em minutos"))
        D = int(input("Informe a distancia em metros"))
        return ((D / 1000) / T)


class CorridaDAO:             # classe estática -> não tem instância
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
        with open("corridas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars, indent=4)
    @classmethod
    def abrir(cls):  #método abrir
        cls.objetos = []
        try:
            with open("corridas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Corrida(dic["id"], dic["nome"])
                    cls.objetos.append(c)
        except:
            pass    

class UI: # classe estática -> não tem instância     
    
    def menu():
        print("Pessoas")
        print("1-Inserir, 2-Listar, 3-Pesquisar")
        print()
        print("Corridas")
        print("4-Inserir, 5-Listar, 6-MenorPace, ")
        print()
        print("7 - Fim")
        return int(input("Informe uma opção: "))           
    def main():
        op = 0
        while op != 6:
            op = UI.menu()
            if op == 1: UI.Pessoa_inserir()
            if op == 2: UI.Pessoa_listar()
            if op == 3: UI.Pessoa_Pesquisar()
            if op == 4: UI.Corrida_inserir()
            if op == 5: UI.Corrida_listar()
            if op == 6: UI.Corrida_menorpace()
            

    def Pessoa_inserir():
        #id = int(input("Informe o id: "))
        id = 0
        nome = input("Informe o nome: ")
        c = Pessoa(id, nome)
        Pessoa.inserir(c)
    def Pessoa_listar():
        for obj in Pessoa.listar():
            print(obj)       
    def Pessoa_Pesquisar():
        UI.Pessoa_Pesquisar()
        id = int(input("Informe o id a ser pesquisado: "))
        nome = ""
        c = Pessoa(id, nome)
        Pessoa.Pesquisar(c)

    def Corrida_inserir():
        id = 0
        descricao = input("Insira a corrida: ")
        c = Corrida(id)
        Corrida.inserir(c)
    def Corrida_listar():
        for obj in Corrida.listar():
            print(obj)       
    def Corrida_menorpace():
        if corrida <= corrida + 1: corrida = corrida
        return("Essa é a corrida com menor pace :)")
    
UI.main()