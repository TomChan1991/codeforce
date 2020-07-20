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

        
        int mI = 0;
        for (int i = 1; i < m; i++){
            cout << s[i].second << "  " << s[mI].second << endl;
            if (s[i].second > s[mI].second)
                mI = i;
            else if (s[i].second == s[mI].second && s[i].first > s[mI].first)
                mI = i;
        }
        
        int res = s[mI].first + s[mI].second * (n - 1), bf = s[mI].second;
        cout << res << endl;
        sort(s.begin(), s.end());
        int i = m -1;
        int cur = 0, bs = 0;
        list<int> qur;
        while (true){
            cur += s[i].first;
            n -= 1;
            bs = max(bs, s[i].second);
            while (!qur.empty() && bs > qur.back()){
                cur -= qur.back();
                qur.pop_back();
                n += 1;
            }
            res = max(res, cur + bs * n);
            qur.push_back(s[i].first);
            i -= 1;
        }
        cout << res << endl;

    }
    return 0;
}