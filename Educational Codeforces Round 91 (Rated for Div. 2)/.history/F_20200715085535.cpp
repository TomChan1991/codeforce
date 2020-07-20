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
    M(int l, int r) : l(l), r(r){}

    void cal(){
        v = pl->v * pr->v;
        _v = pl->_v * pr->v;
        v_ = pl->v * pr->v_;
        _v_ = pl->_v * pr->v_
        int mid = (l + r) / 2
        if (s[mid] == '1'){
            v += pl->v_ * pr->_v * (19 - ((s[mid] -'0') * 10 + s[mid+1] - '0'))
            _v += pl->_v_ * pr->_v * (19 - ((s[mid] -'0') * 10 + s[mid+1] - '0'))
            v_ += pl->v_ * pr->_v_ * (19 - ((s[mid] -'0') * 10 + s[mid+1] - '0'))
            _v_ += pl->_v_ * pr->_v_ * (19 - ((s[mid] -'0') * 10 + s[mid+1] - '0'))
        }
    }
}*root;
 
int n, q;
string s;

M* build(l, r){
    if (l == r){
        return new M(l, l, s[l] - '0' + 1, 1, 1, 0);
    }
    int mid = (l + r) / 2
    M *x =  new M(l, r);
    x->pl = build(l, mid);
    x->pr = build(mid + 1, r)
    x->cal();

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