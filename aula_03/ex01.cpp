#include <iostream>
using namespace std;
int main() {

        int x = 5;
        int y = 5;
        int z = 10;
        int *p  = &x;
        cout << x << "  " << &x << endl;
        cout << y << "  " << &y << endl;
        cout << z << "  " << &z << endl;
        cout << p << "  " << &p << "  " << (*p) << endl;
        return 0;
}
