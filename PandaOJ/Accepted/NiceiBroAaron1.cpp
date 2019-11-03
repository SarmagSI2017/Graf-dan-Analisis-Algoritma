#include<iostream>
#include<algorithm>
using namespace std; 

int main(){
	int a = 0;
	int n;
	cin>>n;
	int c[n];
	for(int i=0;i<n;i++){
		cin>>c[i];
	}
	sort(c, c+n);
	for(int j=1;j<n;j++){
		a+=c[j];
	}
	cout<<endl<<a;
	
	return 0;
}
