class Ingresso:
    def __init__(self): #entidade - tem instâncias
        self.dia = "dom" #atributo
        self.hora = 17
    def inteira(self):
        if self.__dia == "qua": return 8
        if self.__dia in ["seg, ter, qui"]: valor = 16
        else: valor = 20
        if self.__hora == 0 or self.hora >= 17: valor *= 1.5
        return valor
    def meia(self):
        if self.dia == "qua": return 8
        return self.inteira()/ 2

class UI: #interface com o usuário - não tem isntâncias
    @staticmethod
    def main(): #método estático é um método chamado com a classe
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.ingresso()
            if op == 2: UI.Viagem()

    @staticmethod
    def menu():
        print("1-Ingresso, 2-Viagem, 3-Fim1")
        op = int(input("Escolha uma opção"))
        return op

    @staticmethod
    def ingresso(): 
        x = Ingresso() #ingresso. __init__()
        x.dia = input("Informe o dia [dom, seg, ...sab]: ")
        x.hora = int(input("Informe a hora [0-23]: "))
        print(x.dia)
        print(x.hora)
        print(f"Valor da inteira R$ {x.inteira():.2f}")
        #X.inteiro() chama o método da classe e a instância x
        #.inteira 
        print(f"Valor da meia R$ {x.inteira():.2f}")

    @staticmethod
    def viagem():
        pass

UI.main()