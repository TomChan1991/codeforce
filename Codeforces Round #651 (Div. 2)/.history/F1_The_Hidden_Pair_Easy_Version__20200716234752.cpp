#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int, int>
void printq(vector<int> query){
    cout << "? " << query.size() << " "; 
    for (int i : query){
        cout << i << " ";
    }
    cout << endl;
    cout.flush();
}

vector<vector<int>> distance(int node, vector<unordered_set<int>> &edges, int maxD){
    vector<vector<int>> res(maxD + 1);
    vector<int> vis(edges.size(), 0);
    vector<int> qur;
    qur.push_back(node);
    int step = 1;
    while (!qur.empty() && step < res.size()){
        vector<int> nqur;
        for (int i : qur){
            vis[i] = 1;
            for (int j : edges[i]){
                if (vis[j] == 0){
                    nqur.push_back(j);
                    res[step].push_back(j);
                }
            }
        }
        qur = nqur;
        step += 1;
    }
    return res;
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
        vector<int> query(n);
        for (int i = 0; i < query.size(); i++)
            query[i] = i + 1;
        printq(query);
        int node, dis;
        cin >> node >> dis;
        auto d = distance(node, edges, dis);
        int lo = (dis + 1) / 2, hi = dis;
        while (lo < hi){
            int mid = (lo + hi + 1) / 2;
            if (d[mid].empty()){
                hi = mid - 1;
                continue;
            }
            printq(d[mid]);
            int newnode, newdis;
            cin >> newnode >> newdis;
            if (newdis == dis){
                lo = mid;
                node = newnode;
            } else {
                hi = mid - 1;
            }
        }
        d = distance(node, edges, dis);
        printq(d[dis]);
        int onode, odis;
        cin >> onode >> odis;
        cout << "! " << node << " " << onode << endl;
        cout.flush();
        string s;
        cin >> s;
        if (s != "Correct")
            exit(0);

    }
    return 0;
}