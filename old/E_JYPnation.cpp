#include <iostream>
#include <bitset>
#include <cstring>
#include <set>
using namespace std;
set<int> grid[8001];
bool vis[8001];
long long ans = 0;
int main(){
    int n;
    cin >> n;
    for (int i = 0; i != n; i++){
        string x;
        cin >> x;
        for (int j = 0; j < x.size(); j++){
            if (x[j] == '1')
                grid[i].insert(j);
        }
    }
    for (int i = 0; i != n; i++){
        memset(vis, false, 8001);
        vis[i] = true;


        
    }
    return 0;
}