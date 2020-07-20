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
string s;

M* build(l, r){
    if (l == r){
        M *x = new M();
        x->v = int(s[l]) + 1;
    }

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