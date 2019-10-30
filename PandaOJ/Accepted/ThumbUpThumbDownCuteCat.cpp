/*

Thumb Up Thumb Down Cute Cat
https://pandaoj.com/problem/IDEAFUSE18QF
Author : Daffa

INPUT
7 3
2 -1
5 13
10 -4

OUTPUT
YES
NO
NO
YES

*/

#include <iostream>

using namespace std;

int main()
{
    int a,b,check;
    int flag = 0;
    cin >> a;
    cin >> b;
    for(int i = a;i>=0;i--){
        check = a-i;
        if(i-check == b){
            flag = 1;
            break;
        }
    }
    
    if(flag==1){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
    
}