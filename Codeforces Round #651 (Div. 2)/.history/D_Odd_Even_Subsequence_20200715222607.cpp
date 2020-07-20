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
    
    return 0;
}