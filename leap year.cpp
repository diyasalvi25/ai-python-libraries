#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "Enter any year:\n";
    cin >> year;

    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
        cout << year << " is a Leap Year.";
    else
        cout << year << " is not a Leap Year.";

    return 0;
}
