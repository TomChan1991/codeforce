#include <iostream>
#include <list>
#include <vector>
#include <math.h>
using namespace std;
int cnt[2001];
vector<int> child[2001];
int a[2001];
int v = 1;

int main(){
    int n;
    cin >> n;
    n += 1;
    int root = 1;
    a[1] = 1;
    for (int i = 1; i < n; i++){
        a[i] = -1;
        int p;
        cin >> p >> cnt[i];
        if (p == 0) root = i;
        else child[p].push_back(i);
    }
    list<int> que;
    for (int i = 1; i < n; i++){
        if (child[i].empty()){
            que.push_back(i);
        }
    }
    

    cout << "YES" << endl;
    for (int i = 1; i < n - 1; i++)
        cout << a[i] << ' ';
    cout << a[n-1];
    return 0;
}