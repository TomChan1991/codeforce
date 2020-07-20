#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int, int>
void printq(vector<int> query, int type = 1){
    if (type == 1)
        cout << "? ";
    else 
        cout << "! ";
    for (int i : query){
        cout << i << " ";
    }
    cout << endl;
}
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
        int pnode = INT32_MAX, pdis = INT32_MAX;
        for (int __ = 0; __ < 14; __++){
            vector<int> query;
            for (int i = 0; i < edges.size(); i++){
                if (edges[i].size() == 1){
                    query.push_back(i);
                }
            }
            if (query.size() == 2){
                printq(query);
            } else {
                
            }
            cout.flush();
        }   
    }
    return 0;
}