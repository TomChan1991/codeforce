#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int, int>
int minimunMove(string &s, int start, int end, char c){
    if (end - start == 1){
        if (s[start]  == c)
            return 0;
        else
            return 1;
    }
    int mid = (end + start) / 2;
    int res = INT32_MAX, cnt = 0;
    for (int i = 0; i < mid; i++){
        if (s[i] != c)
            cnt += 1;
    }
    res = cnt + minimunMove(s, mid, end, char(c + 1));
    cnt = 0;
    for (int i = mid; i < end; i++){
        if (s[i] != c)
            cnt += 1;
    }
    res = min(res,  cnt + minimunMove(s, start, mid, char(c + 1)));
    // cout << s.substr(start, end-start) << " " << res << " " << c <<endl;;
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
        string s;
        cin >> s;
        cout << minimunMove(s, 0, n, 'a') << endl;


    }
    return 0;
}