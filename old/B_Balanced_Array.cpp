// http://codeforces.com/problemset/problem/1343/B
#include <iostream>
using namespace std;
int main(){
    int time;
    cin >> time;
    for (int i = 0; i < time; i++){
        int x;
        cin >> x;
        if (x % 4 != 0){
            cout << "NO" << endl;
            continue;
        }
        cout << "YES" << endl;
        for (int j = 0; j < x / 2; j++){
            cout << (j + 1) * 2 << " ";
        }
        for (int j = 0; j < x / 2 - 1; j++){
            cout << 2 * j + 1 << " ";
        }
        cout << x + (x / 2) - 1 << endl;

    }
    return 0;
}