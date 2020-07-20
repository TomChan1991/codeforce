#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
#define endl '\n'
#define ll long long
#define pi pair<int, int>
#define f first
#define s second
 
const int mod = 998244353;
 
struct M{
	ll v, _v, v_, _v_;
	int l, r;
    M *pl, *pr;
};
 
int n, q;
string s
 
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> n >> q;
	n++;
	
	for(int i = 1; i < n; i++){
		char c;
		cin >> c;
		a[i] = c - '0';
		T[mxn + i] = M(a[i - 1], a[i]);
	}
	
	for(int i = mxn - 1; i; i--) T[i] = T[i << 1 | 1] * T[i << 1];
	
	while(q--){
		int x, y;
		cin >> x >> y;
		a[x] = y;
		for(int t = 0; t <= (x != n - 1); t++){
			T[mxn + x + t] = M(a[x + t - 1], a[x + t]);
			for(int i = (mxn + x + t) >> 1; i; i >>= 1) T[i] = T[i << 1 | 1] * T[i << 1];
		}
		cout << T[1].aa << endl;
	}
 
	return 0;
}