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
        vector<int> nums(n);
        for (int i = 0; i < n; i++)
            cin >> nums[i];
        int end = n - 2;
        while (end >= 0 && nums[end] <= nums[end + 1])
            end -= 1;
        while (end >= 0 && nums[end] >= nums[end+1])
            end -= 1;
        cout << end + 1 << endl;

    }
    return 0;
}