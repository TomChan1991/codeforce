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
        cin >> n;
        vector<int> r1(n), r2(n);
        for (int i = 0; i < n; i++)
            cin >> r1[i];
        for (int i = 0; i < n; i++)
            cin >> r2[i];
        vector<vector<int>> pos(n + 1);
        for (int i = 0; i < n; i++){
            pos[r1[i]].push_back(i);
            pos[r2[i]].push_back(i);
        }
        vector<vector<pi>> edges(n + 1);
        bool flag = true;
        for (int i = 1; i < n + 1; i++){
            if (pos[i].size() != 2){
                flag = false;
                break;
            }
            if (pos[i][0] == pos[i][1] )
                continue;
            if (r1[pos[i][0]] == i && r1[pos[i][1]] == i){
                edges[pos[i][0]].push_back(pi(pos[i][1], 1));
                edges[pos[i][1]].push_back(pi(pos[i][0], 1));
            } else {
                edges[pos[i][0]].push_back(pi(pos[i][1], 0));
                edges[pos[i][1]].push_back(pi(pos[i][0], 0));
            }
            
        }
        if (!flag){
            cout << -1 << endl;
            continue;
        }
        vector<int> vis(n + 1, false);
        list<int> res ;
        for (int i = 1; i < n + 1; i++){
            if (vis[i]) continue;
            vector<vector<int>> color(2);
            color[0].push_back(i);
            list<pi> que;
            que.push_back(pi(i, 0));
            vis[i] = true;
            while (!que.empty()){
                auto x = que.front();
                que.pop_front();
                for (auto e : edges[x.first]){
                    if (!vis[e.first]){
                        vis[e.first] = true;
                        int c = x.second ^ e.second;
                        que.push_back(pi(e.first, c));
                        color[c].push_back(e.first);
                    }
                }
            }
            if (color[0].size() < color[1].size()){
                for (int i : color[0]) res.push_back(i);
            } else {
                for (int i : color[1]) res.push_back(i);
            }
        }
        cout << res.size() << endl;
        for (int i : res)   
            cout << i << " ";
        cout << endl;

    }
    return 0;
}