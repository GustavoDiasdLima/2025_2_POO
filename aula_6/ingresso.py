class Ingresso:              # entidade - tem instâncias
    def __init__(self):
        self.__dia = "dom"   # definição dos atributos
        self.__hora = 17

    def get_dia(self):       # get - retorna o valor atual do atributo
        return self.__dia
    def get_hora(self):
        return self.__hora   

    def set_dia(self, dia):  # set - altera o valor do atributo
        # testar o valor do dia para armazenar apenas valores válidos
        if dia in ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]:
            self.__dia = dia
        else: raise ValueError("Dia inválido") # dê um erro
    def set_hora(self, hora):
        # testar o valor da hora para armazenar apenas valores válidos
        if hora >= 0 and hora <= 23: self.__hora = hora
        else: raise ValueError("Horá inválida") # dê um erro

    def inteira(self):     # método de instância. self é a instância que chamou a operação
        if self.__dia == "qua": return 8
        if self.__dia in ["seg", "ter", "qui"]: valor = 16
        else: valor = 20
        if self.__hora == 0 or self.__hora >= 17: valor *= 1.5
        return valor 
    def meia(self):
        if self.__dia == "qua": return 8
        return self.inteira()/2

"""
x = Ingresso()
y = Ingresso()
print(id(x))
print(id(y))
"""