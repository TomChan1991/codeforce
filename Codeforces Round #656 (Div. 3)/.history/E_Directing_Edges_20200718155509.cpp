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
        int n, m;
        cin >> n >> m;
        printf("%d, %d", n, m);
        vector<unordered_set<int>> from(n + 1);
        vector<unordered_set<int>> to(n + 1);
        vector<unordered_set<int>> und(n + 1);
        vector<pi> res;
        for (int i = 0; i < m; i++){
            int t, x, y;
            cin >> t >> x >> y;
            if (t == 1){
                from[x].insert(y);
                to[y].insert(x);
                res.push_back(pi(x, y));
            } else {
                und[x].insert(y);
                und[y].insert(x);
            }
        }
        list<int> qur;
        for (int i = 1; i < n + 1; i++ ){
            if (from[i].size() == 0)
                qur.push_back(i);
        }
        while (!qur.empty()){
            int index = qur.front();
            qur.pop_front();
            for (int i : und[index]){
                res.push_back(pi(index, i));
                und[i].erase(index);
            }
            for (int i : to[index]){
                from[i].erase(index);
                if (from[i].size() == 0){
                    qur.push_back(i);
                }
            }

        }
        if (res.size() == m){
            cout << "YES" << endl;
            for (auto p : res){
                cout << p.first << " " << p.second << endl;
            }
        } else {
            cout << "No" << endl;
        }

    }
    return 0;
}