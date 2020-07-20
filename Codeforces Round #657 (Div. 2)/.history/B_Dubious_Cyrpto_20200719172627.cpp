#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int, int>
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t-- > 0){
        int l, r, m;
        cin >> l >> r >> m;
        int a = l, b, c;
        while (true){
            int rest = m % a;
            if (rest <= (r - l) ){
                cout << a  << " " << l + rest << " " << l << endl;
                break;
            } else if ((a - rest)<= (r - l)){
                cout << a  << " " << r - (a - rest) << " " << r << endl;
                break;
            }
            a += 1;
        }
    }
    return 0;
}