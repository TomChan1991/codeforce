#include <bits\stdc++.h>
using namespace std;
struct Node{
    int v;
    Node *l, *r;
}*root;
int main(){
    // root = Node();
    root = new Node();
    root->v = 10;
    cout << root->v;

    return 0;
}