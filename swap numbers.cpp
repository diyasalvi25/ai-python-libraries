#include <iostream>
using namespace std;
int main() {
    int a = 10, b = 20;

    cout << "Before swap: a = " << a << ", b = " << b << endl;
    int temp = a; 
    a = b;       
    b = temp;    
    cout << "After swap: a = " << a << ", b = " << b << endl;
    return 0;
}
