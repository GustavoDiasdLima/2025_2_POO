#include <iostream>
using namespace std;

class Conta {
    public:
    string titular;
    string numero;
    double saldo;
    Conta() {                       //construtor

        titular = "sem nome";   //atributos
        numero = "sem número";
        saldo = 0;
    }
    void depositar(double valor) {
        saldo += valor;
    }
    void sacar(double valor) {
        saldo -= valor;
    }
};

int main() {
Conta x; //é uma instancia
cout << x.titular << " " << x.numero << " " << x.saldo << endl;
x.titular = "Raquel";
x.numero = "123-x";
x.saldo = 1000;
cout << x.titular << " " << x.numero << " " << x.saldo << endl;
x.depositar(500);
cout << x.titular << " " << x.numero << " " << x.saldo << endl;
return 0;
}
