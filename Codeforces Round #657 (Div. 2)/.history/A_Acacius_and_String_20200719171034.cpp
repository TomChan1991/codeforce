#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int, int>
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    string mod = "abacaba";
    while (t-- > 0){
        int n;
        cin >> n;
        string s;
        cin >> s;
        bool flag = true;
        for (int i = 0; i <= s.size() - 7; i++){
            flag = true;
            for (int j = 0; j < 7; j++){
                if (s[i + j] != '?' && s[i+j] != mod[j]){
                    flag = false;
                    break;
                }  
            }
            if (flag){
                for (int j = 0; j < 7; j++)
                    s[i+j] = mod[j];
            }
        }
        if (flag){
            for (int i = 0; i < s.size(); i++)
                if (s[i] == '?')
                    s[i] = 'a';
            cout << "YES" << endl;
            cout << s << endl;
        } else {
            cout << "No" <<endl;
        }
    } 
    return 0;
}