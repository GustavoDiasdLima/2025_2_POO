#import ingresso
from ingresso import Ingresso

class UI:       # interface com o usuário -  não tem instância
    @staticmethod
    def main(): # método estático é um método chamado com a classe 
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.ingresso()  # ingresso é chamado com a classe UI
            if op == 2: UI.viagem()
    @staticmethod
    def menu():
        print("1-Ingresso, 2-Viagem, 3-Fim")
        op = int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def ingresso():
        x = Ingresso()   # Ingresso.__init__()
        #print(x.dia)  # __dia não é visível fora da classe Ingresso
        #print(x.hora) # está encapsulado (começa com __)
        print(x.get_dia())
        print(x.get_hora())

        #x.dia = input("Informe o dia [dom, seg, ... sab]: ")
        #x.hora = int(input("Informe a hora [0-23]: "))
        x.set_dia(input("Informe o dia [dom, seg, ... sab]: "))
        x.set_hora(int(input("Informe a hora [0-23]: ")))

        #print(x.dia)
        #print(x.hora)
        # x.inteira() chama o método da classe e self é a instância x
        # inteira() é chamado com a instância x 
        print(f"Valor da inteira R$ {x.inteira():.2f}")
        print(f"Valor da meia R$ {x.meia():.2f}")
    @staticmethod
    def viagem():
        pass

UI.main()