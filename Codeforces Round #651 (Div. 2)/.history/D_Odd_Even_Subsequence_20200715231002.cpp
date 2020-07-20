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
    int lo = 1, hi = pow(10, 9);
    while (lo < hi){
        int mid = lo + (hi - lo) / 2;
        if (n == )
        cout << mid << endl;
        bool flag = false;
        //even
        int cnt = 0;
        for (int i = 0; i < n; i++){
            if (nums[i] <= mid){
                cnt += 1;
                i++;
                if (cnt * 2 >= k){
                    flag = true;
                    break;
                } 
            } 
        }
    
        if (!flag && k > 1){ //odd
            cnt = 0;
            for (int i = 1; i < n; i++){
                if (nums[i] <= mid){
                    cnt += 1;
                    i++;
                } 
                if (cnt * 2 + 1 >= k){
                    flag = true;
                    break;
                }
            }
        }
        if (!flag){
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    cout << hi << endl;
    return 0;
}