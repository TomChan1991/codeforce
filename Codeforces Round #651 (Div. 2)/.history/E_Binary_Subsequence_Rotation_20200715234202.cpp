#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int, int>
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    string s, t;
    cin >> s >> t;
    int a01 = 0, a10 = 0, res = 0, cnt = 0;
    for (int i = 0; i < n; i++){
        if (s[i] != t[i]){
            if (s[i] == '1'){
                if (a01 > 0){
                    a01 -= 1;
                    
                } else{
                    res += 1;
                }
                a10 += 1;
                cnt += 1;
            } else {
                if (a10 > 1){
                    a10 -= 1;
                } else {
                    res += 1;
                }
                a01 += 1;
                cnt -= 1;
            }
            
        }
    }
    if (cnt != 0){
        cout << -1 << endl;
    } else {
        cout << res << endl;
    }
    return 0;
}