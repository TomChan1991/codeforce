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
        int cnt = 0;
        for (int i = 0; i <= s.size() - 7; i++){
            flag = true;
            for (int j = 0; j < 7; j++){
                if (s[i+j] != mod[j]){
                    flag = false;
                    break;
                }  
            }
            if (flag){
                cnt += 1;
            }
        }
        if (cnt > 1){
            cout << "No" <<endl;
        } else if (cnt == 1){
            for (int i = 0; i < s.size(); i++)
                if (s[i] == '?')
                    s[i] = 'z';
            cout << "YES" << endl;
            cout << s << endl;
        } else {
            for (int i = 0; i <= s.size() - 7; i++){
                flag = true;
                for (int j = 0; j < 7; j++){
                    if (s[i + j] == '?' || s[i+j] != mod[j]){
                        flag = false;
                        break;
                    }  
                }
                if (flag){
                    flag = false;
                    for (int j = 0; j < 7; j++){
                        if (s[i + 4 + j] != mod[j]){
                            flag = true;
                            break;
                        }
                    }
                    if (flag){
                        for (int j = 0; j < 7; j++){
                            if (s[i+j] == '?')
                                s[i + j] = mod[j];
                        }
                        break;
                    }
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
        
    } 
    return 0;
}