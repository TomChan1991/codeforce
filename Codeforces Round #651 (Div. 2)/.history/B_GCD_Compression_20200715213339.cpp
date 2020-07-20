#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int, int>
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t, n;
    for (int i = 0; i < t; i++){
        int odd = -1, even = -1;
        cin >> n;
        int cnt = 0;
        for (int j = 1; j <= 2 * n && cnt < n - 1; j++){
            int num;
            cin >> num;
            if (num % 2 == 0){
                if (even > 0){
                    cout << even << " " << j  << endl;
                    even = -1;
                    cnt += 1;
                } else {
                    even = j;
                }
            } else {
                if (odd > 0){
                    cout << odd << " " << j << endl;
                    odd = -1;
                    cnt += 1;
                } else {
                    odd = j;
                }
            }
        }
    }
    return 0;
}