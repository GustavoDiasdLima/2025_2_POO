class Cliente:
    def __init__(self, nome , limite, socio):
        self.set_nome(nome)
        self.set_limite(limite)
        self.__socio = None
    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_limite(self, limite):
        self.__limite = limite
    def get_limite(self):
        return self.__nome
    def set_nome(self, socio):
        self.__socio = socio
    def get_socio(self):
        return self.__socio
 
    def __str__(self):
        if self.__socio == None:
            return f"{self._nome} {self.__limite} {self.get_limite()}"
        else:
            return f"{self.__nome} {self.__limite} {self.__socio.__nome} {self.get_limite()}"

class UI:
    @staticmethod


