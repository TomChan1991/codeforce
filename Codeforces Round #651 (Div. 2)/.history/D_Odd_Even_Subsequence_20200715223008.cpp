#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int, int>
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k;
    cin >> n >> k;
    vector<int> nums(n);
    for (int i = 0; i < n; i++){
        cin >> nums[i];
    }
    vector<pi> dp(k + 1, pi(INT32_MAX, INT32_MAX));
    dp[0] = pi(0, 0);
    for (int i : nums){
        for (int j = k; j >= 0; j--){
            if (j % 2 == 0){
                dp[j].first = min(max(dp[j-1].first, i), dp[j].first);
            } else {
                dp[j].second = min(max(dp[j-1].second, i), dp[j].second);
            }
        }
    }
    cout << min(dp[k].first, dp[k].second) << endl;
    return 0;
}