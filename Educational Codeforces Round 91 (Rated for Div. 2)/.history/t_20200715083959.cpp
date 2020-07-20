#include <bits\stdc++.h>
using namespace std;
struct Node{
    int v;
    Node *l, *r;
}*root;
int main(){
    // root = Node();
    root = new Node();
    Node x;
    x.v = 100;
    root->v = 10;
    cout << root->v << ' ' << x.v;

    return 0;
}