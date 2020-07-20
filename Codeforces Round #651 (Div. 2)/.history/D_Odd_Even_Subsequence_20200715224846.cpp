#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int, int>
void p(vector<pi> n){
    for (pi p : n ){
        cout << p.first << " " << p.second << endl;
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k;
    cin >> n >> k;
    vector<int> nums(n);
    for (int i = 0; i < n; i++){
        cin >> nums[i];
    }
    if (k == 1){

    }
    vector<pi> dp(k + 1, pi(INT32_MAX, INT32_MAX));
    dp[0] = pi(0, 0);
    // dp[1] = pi(0, INT32_MAX);
    for (int i : nums){
        for (int j = k; j > 0; j--){
            if (j % 2 == 1 && (i < dp[j].first or dp[j-1].second < min(dp[j].second, dp[j].first))){
                dp[j] = dp[j - 1];
                dp[j].first = max(dp[j].first, i);
            } else if (j % 2 == 0 && (i < dp[j].second or dp[j-1].first < min(dp[j].second, dp[j].first))) {
                dp[j] = dp[j - 1];
                dp[j].second = max(dp[j].second, i);
            }
        }
        p(dp);
    }
    cout << min(dp[k].first, dp[k].second) << endl;
    return 0;
}