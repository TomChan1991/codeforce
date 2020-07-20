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
        vector<int> appear(n+1, false);
        vector<int> res;
        for (int i = 0; i < 2 * n; i++){
            int x;
            cin >> x;
            if (!appear[x]){
                appear[x] = true;
                res.push_back(x);
            }
        }
        for (int i : res)
            cout << i << " ";
        cout << endl;
    }
    return 0;
}