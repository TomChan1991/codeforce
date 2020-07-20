#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int, int>
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t, n;
    cin >> t;
    for (int i = 0; i < t; i++){
        cin >> n;
        if (n % 2 == 0){
            cout << n / 2 << endl;
        } else{
            cout << (n - 1) / 2 << endl;
        }
    }
    return 0;
}