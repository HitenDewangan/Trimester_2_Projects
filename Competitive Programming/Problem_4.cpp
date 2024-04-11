/*Given three numbers a, b and m. Calculate (a(to the power b) % m)

Example input :
2 5 3

Example output :
2

Explanation :
25 % 3 = 32 % 3 = 2
*/

#include <iostream>
using namespace std;

int powerModulo(int a, int b, int m) {
    int result = 1;
    a = a % m;

    while(b > 0) {
        if (b % 2 == 1) {
            result = (result * a) % m;
        }

        b /= 2;
        a = (a * a) % m;
    }

    return result;
}

int main() {
    int a, b, m;

    cin >> a >> b >> m;

    int result = powerModulo(a, b, m);

    cout << "Result is : " << result << endl;

    return 0;
}
