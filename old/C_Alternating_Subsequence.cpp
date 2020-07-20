// http://codeforces.com/problemset/problem/1343/C
#include <iostream>
#include <math.h>
using namespace std;
int main(){
    int time;
    cin >> time;
    for (int i = 0; i < time; i++){
        long long n, cur, sum = 0; 
        cin >> n >> cur;
        for (int j = 1; j < n; j++){
            long long x;
            cin >> x;
            if (x * cur > 0){
                cur = max(cur, x);
            } else {
                sum += cur;
                cur = x;
            }
        }
        cout << sum + cur << endl;
    }
    return 0;
}