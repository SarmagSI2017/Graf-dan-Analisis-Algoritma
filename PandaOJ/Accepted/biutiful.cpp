//auth: adit ganteng


#include<stdio.h>
#include<iostream>
#include <bits/stdc++.h> 
using namespace std; 
int main(){
int t,i,tot,masuk;
scanf("%d",&t);
string s[t]={};
for(i=0;i<t;i++)
{
    scanf("%d",&masuk);
    int r=1;
    tot=0;
    while(tot<masuk){
        tot+=r;
        r+=1;
        if(tot==masuk){
            s[i]="YES";
            break;
        }
        if(tot>masuk){
            s[i]="NO";
            break;
        }


    }

}

for(i=0;i<t;i++){
    cout<<"Case #"<<i+1<<": "<<s[i]<<"\n";

}

}
