#include <iostream>
using namespace std;

int main() {
    int rows;
    cout << "Rows for pattern: ";
    cin >> rows;

    for (int i = rows; i >= 1; i--) { 
        for (int j = 1; j <= i; j++) { 
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
