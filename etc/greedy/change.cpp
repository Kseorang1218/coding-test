#include <bits/stdc++.h>  // 사람들이 많이 사용하는 표준 라이브러리 헤더들을 모두 한 번에 Compile될 수 있도록 해 둔 것이죠. 

using namespace std;

int n=1260;
int cnt;

int coinTypes[4]={500, 100, 50, 10};

int main(){
    for (int i=0; i<4; i++){
        int coin = coinTypes[i];
        cnt += n/coin;
        n = n%coin;
    }
    cout << cnt << '\n';
    // cout: <iostream>에 미리 만들어져 있는 전역 객체(변수)
}