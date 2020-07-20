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
    int cnt = 0, res = 0;
    for (int i = 0; i < n; i++){
        if (s[i] != t[i]){
            if (s[i] == '1'){
                cnt += 1;
            } else {
                cnt -= 1;
            }
            printf("i:%d, cnt:%d\n", i, cnt);
            res = max(res, abs(cnt));
        }
    }
    if (cnt != 0){
        cout << -1 << endl;
    } else {
        cout << res << endl;
    }
    return 0;
}