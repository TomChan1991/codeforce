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
        int x, y, z;
        cin >> x >> y >> z;
        int a = x;
        if (x == y && x >= z){
             cout <<"Yes" <<endl;
            cout << x <<" " << z << " " << z << endl;
        } else if (x == z && x >= y){
            cout <<"Yes" <<endl;
            cout << y << " " << x << " " << y << endl;
        } else if (y == z && y >= x){
            cout <<"Yes" <<endl;
            cout << x << " " << x << " " y << endl;
        } else {
            cout << "No" << endl;
        }
    }
    return 0;
}