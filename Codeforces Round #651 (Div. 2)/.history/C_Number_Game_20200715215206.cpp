#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int, int>
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    for (int _ = 0; _ < t; _++){
        int n;
        cin >> n;
        while (n % 2 == 0){
            n = n / 2;
        };
        if (n == 1){
            cout << "FastestFinger" << endl;
        } else if (n % 2 == 1 || n == 2){
            cout << "Ashishgup" << endl;
        } else {
            int a = n;
            while (a % 2 == 0){
                a /= 2;
            }
            if (a == 1){
                cout << "FastestFinger" << endl;
            }

        }
    }
    return 0;
}