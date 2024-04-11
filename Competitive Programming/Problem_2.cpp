/*Given a number N, Print first N prime number starting from 2 and skipping every
alternate prime number

Example Input:
5

Example Output:
2 5 11 17 23

Explanation :
▪ First few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 …
▪ First five alternate prime numbers will be 2, 5, 11, 17, and 23
*/

#include<iostream>
using namespace std;

#include <iostream>
#include <vector>

using namespace std;

bool isPrime(int num) {
    if (num < 2) {
        return false;
    }

    for (int i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

void printAlternatePrimes(int N) {
    vector<int> primes;
    int currentNumber = 2;

    while (primes.size() < 2*N) {
        if (isPrime(currentNumber)) {
            primes.push_back(currentNumber);
        }

        currentNumber++;
    }

    for (size_t i = 0; i < primes.size(); i += 2) {
        cout << primes[i] << " ";
    }
    cout << endl;
}

int main(){
    int n;
    cin>>n;

    printAlternatePrimes(n);

}