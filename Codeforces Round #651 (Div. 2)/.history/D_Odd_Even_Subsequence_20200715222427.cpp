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
    cout << nums[0];
    return 0;
}