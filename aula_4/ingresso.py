class Ingresso:
    def __init__(self): #entidade - tem instâncias
        self.dia = "dom" #atributo
        self.hora = 17
    def inteira(self):
        if self.dia == "qua": return 8
        if self.dia in ["seg, ter, qui"]: valor = 16
        else: valor = 20
        if self.hora == 0 or self.hora >= 17: valor *= 1.5
        return valor
    def meia(self):
        if self.dia == "qua": return 8
        return self.inteira()/ 2