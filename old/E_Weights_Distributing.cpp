// http://codeforces.com/problemset/problem/1343/E
#include <bits/stdc++.h>
using namespace std;

vector<long long> bfs(vector<vector<int>>& grid, int start, int end){
    deque<int> que;
    
    que.push_back(start);
    int step = 0;
    vector<long long > vis(grid.size(), -1);
    vis[start] = 0;
    if (start == end) return vis;
    while (!que.empty()){
        int size = que.size();
        for (int _  = 0; _ < size; _++){
            int x = que.front();
            que.pop_front();
            for (int i : grid[x]){
                if (vis[i] == -1){
                    vis[i] = step+1;
                    que.push_back(i);
                    if (i == end){
                        return vis;
                    }

                }
            }
        }
        step += 1;
    }
    return vis;
}

bool cmp(vector<long long>&a, vector<long long>&b){
    return a[0] < b[0];
}

int main(){
    int time;
    cin >> time;
    for (int _ = 0; _ < time; _++){
        int n, m, a, b, c;
        cin >> n >> m >> a >> b >> c;
        a--, b--, c--;
        vector<vector<int>> grid(n);
        vector<int> price(m);
        for (int i = 0; i < m; i++){
            cin >> price[i];
        }
        for (int i = 0; i < m; i++){
            int x, y;
            cin >> x >> y;
            x--, y--;
            grid[x].push_back(y);
            grid[y].push_back(x);
        }
        sort(price.begin(), price.end());
        vector<long long> sp(price.size() + 1, 0);
        for (int i = 1; i < sp.size(); i++){
            sp[i] = sp[i-1] + price[i-1];
        }
        vector<long long > disa = bfs(grid, a, -1);
        vector<long long > disb = bfs(grid, b, -1);
        vector<long long > disc = bfs(grid, c, -1);
        long long res = INT64_MAX;
        for (int i = 0; i < n; i++){
            if (disa[i] + disb[i] + disc[i] > m) continue;
            res = min(res, sp[disa[i] + disb[i] + disc[i]] + sp[disb[i]]);
        }
        cout << res << endl;

    }
    return 0;
}