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
        int n, m;
        cin >> n >> m;
        vector<int> f(m), s(m);
        for (int i = 0; i < m; i++)
            cin >> f[m] >> s[m];
        int mI = 0;
        for (int i = 0; i < m; i++){
            if (s[i] > s[mI])
                mI = i;
            else if (s[i] == s[mI] && h[i] > h[mI])
                mI = i;
        }
        int sf = f[mI];
        
    }
    return 0;
}