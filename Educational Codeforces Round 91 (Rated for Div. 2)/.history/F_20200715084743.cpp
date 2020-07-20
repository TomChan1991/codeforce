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
    M(int l, int r, int v, int _v, int v_, int _v_) : v(v), l(l), r(r), _v(_v), _v_(_v_), v_(v_) {}
};
 
int n, q;
string s;

M* build(l, r){
    if (l == r){
        M *x = new M();
        x->v = s[l] - '0' + 1;
        x->_v = 1;
        x->_v_ = 0;
        x->v_ = 1;
        return x;
    }
    int mid = (l + r) / 2
    M *pl = 

}

void update(M *l){

}
 
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> n >> q >> s;
	
	while(q--){
		int x, y;
		cin >> x >> y;
		s[x-1] = y;
		
	}
 
	return 0;
}