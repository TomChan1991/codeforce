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
        int n, m;
        cin >> n >> m;
        vector<pi> s(m);
        for (int i = 0; i < m; i++)
            cin >> s[i].first >> s[i].second;
        
        int res = 0;
        sort(s.begin(), s.end());
        int i = m -1;
        int cur = 0, bs = 0, needf = 0;W
        list<int> qur;
        n -= 1;
        while (i >= 0){
            if (s[i].second > bs){
                bs = s[i].second;
                needf = s[i].first;
                while (!qur.empty() && bs >= qur.back()){
                    cur -= qur.back();
                    qur.pop_back();
                    n += 1;
                }
                res = max(res, cur + bs * n + needf);
            } else if (s[i].first > bs){
                qur.push_back(s[i].first);
                cur += s[i].first;
                n -= 1;
                res = max(res, cur + bs * n + needf);
            }
            
            i -= 1;
        }
        cout << res << endl;

    }
    return 0;
}