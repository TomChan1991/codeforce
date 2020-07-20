#include <iostream>
#include <vector>
#include <set>
#include <list>
#include <math.h>
using namespace std;
vector<set<int>> graph[15001];
vector<int> grid[15001];
int travals[15001][2];
int m, n, k;
set<long long> ans;
set<int> con(int node, int p){
    set<int> all;
    all.insert(node);
    for (int i : grid[node]){
        if (i == p) continue;
        auto c = con(i, node);
        all.insert(c.begin(), c.end());
        graph[node].push_back(c);
    }
    return all;
}

vector<int> run(int node, vector<int> p, int par){
    vector<int> tempnode;
    for (int i = 0; i < m; i++){
        if (p[i] >= k)
            tempnode.push_back(i);
    }
    for (int i = 0; i < tempnode.size(); i++){
        for (int j = i + 1; j < tempnode.size(); j++)
            ans.insert((long long)tempnode[i] * 1000000 + tempnode[j]);
    }
    int z = 0;
    for (int i = 0; i < grid[node].size(); i++){
        if (grid[node][i] == par) continue;
        auto edge = graph[node][z++];
        vector<int> temp = p;
        for (int j = 0; j < m; j++){
            auto t = travals[j];
            auto x = edge.find(t[0]), y = edge.find(t[1]);
            if (x == edge.end() && y != edge.end() || y == edge.end() && x != edge.end()) 
                temp[j] += 1;
            else {
                temp[j] = 0;
            }            
        }
        auto xx = run(grid[node][i], temp, node);
        for (int j = 0; j < m; j++){
            p[j] = max(p[j], xx[j]);
        }
    }
    
    return p;
}

int main(){
    cin >> n >> m >> k;
    
    for (int i = 0; i < n-1; i++){
        int s, t;
        cin >> s >> t;
        grid[s].push_back(t), grid[t].push_back(s);
    }
    for (int i = 0; i < m; i++){
        int s, t;
        cin >> travals[i][0] >> travals[i][1];
    }
    n++;
    con(1, -1);
    run(1, vector<int>(m, 0), -1);
    cout << ans.size();
    return 0;
}