class Conta:
    def __init__(self):   #Construtor
        self.titular = "" #atributos definir dentro do init
        self.numero = ""
        self.saldo = 0  
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, saldo):
        self.saldo -= valor

x = Conta()
print(x.titular, x.numero, x.saldo)
x.titular = "Raquel"
x.numero = "123-x"
x.saldo = 1000
print(x.titular, x.numero, x.saldo)
x.depositar(500)
print(x.titular, x.numero, x.saldo)
