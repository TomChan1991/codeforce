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
        vector<unordered_set<int>> edges(n + 1);
        for (int i = 1; i < n; i++){
            int u, v;
            cin >> u >> v;
            edges[u].insert(v), edges[v].insert(u);
        }
        cout.flush();
    }
    return 0;
}