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
        int n, k;
        cin >> n >> k;
        vector<int> r1, r2;
        for (int i = 0; i < n; i++)
            cin >> r1[i];
        for (int i = 0; i < n; i++)
            cin >> r2[i];
        vector<vector<int>> pos(n + 1);
        for (int i = 0; i < n; i++){
            pos[r1[i]].push_back(i);
            pos[r2[i]].push_back(i);
        }
        vector<vector<p>> edges;


    }
    return 0;
}