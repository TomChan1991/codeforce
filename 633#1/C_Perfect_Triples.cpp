#include <iostream>
#include <math.h>
using namespace std;
int main(){
    int times;
    cin >> times;
    int con[] = {0, 2, 3, 1};
    for (int i = 0; i != times; i++){
        long long n;
        cin >> n;
        if (n <= 4){
            cout << n<<endl;
            continue;
        }
        n = n - 1;
        long long a = n / 3, b =  n % 3;
        long long l = ceil(log(3 * a + 2) / log(4)) - 1;
        long long base = pow(4, l);
        a -= (pow(4, l) - 1) / 3;
        long long f = base + a ;
        if (b == 0){
            cout << f<<endl;
            continue;
        }
        long long res = 2 * base;
        base = base / 4;
        while (base >= 1){
            long long x = a / base;
            long long a = a % base;
            res += con[x] * base;
            base = base / 4;
        }
        
        if (b == 1)
            cout << res << endl;
        else
            cout << (f ^ res) << endl;
    }
    return 0;
}