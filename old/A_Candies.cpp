// http://codeforces.com/problemset/problem/1343/A
#include <iostream>
using namespace std;
int main(){
    int time;
    cin >> time;
    for (int i = 0; i < time; i++){
        long long n;
        cin >> n;
        long long base = 4;
        while (n % (base - 1) != 0){
            base *= 2;
        }
        cout << (n / (base - 1)) << endl ;
    }
    return 0;
}