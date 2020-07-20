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
        sort(f.begin(), f.end());
        sort(s.begin(), s.end());
        int i = m -1, j = m -1;
        ll res = 0;
        while (i >= 0 ) 
    }
    return 0;
}