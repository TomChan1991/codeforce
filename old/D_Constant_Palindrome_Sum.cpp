// http://codeforces.com/problemset/problem/1343/D
#include <bits/stdc++.h>
using namespace std;

int cmp(vector<int>& a, vector<int>& b){
    return a[1] > b[1];
}

int main(){
    int time;
    cin >> time;
    for (int i = 0; i < time; i++){
        int n, K;
        cin >> n >> K;
        vector<int> num(n);
        for (int j = 0; j < n; j++){
            cin >> num[j];
        }
        int res = n / 2;
        map<int, int> memo;
        for (int j = 0; j < n / 2; j++){
            memo[num[j] + num[n-j-1]] += 1;
            // cout << "num" << (num[j] + num[n-j-1]) << endl; 
        }
        vector<vector<int>> x(memo.size(), vector<int>(2));
        int index = 0;
        for (auto p : memo){
            x[index][0] = p.first;
            x[index++][1] = p.second;
        }
        sort(x.begin(), x.end(), cmp);
        // for (auto p : x)
        //     cout << p[0] << "  " << p[1]<< endl;
        for (int j = 0; j < x.size(); j++){
            int cur = 0;
            if (n / 2 - x[j][1] >= res){
                break;
            }
            for (int k = 0; k < n /2; k++){
                if (num[k] + num[n-k-1] == x[j][0]){
                    continue;
                } else if (K + max(num[k], num[n-k-1])>= x[j][0] && 1 + min(num[k], num[n-k-1]) <= x[j][0]){
                    cur += 1;
                } else {
                    cur += 2;
                }
            } 
            res = min(cur, res);
        }
        cout << res << endl;
        

    }
}