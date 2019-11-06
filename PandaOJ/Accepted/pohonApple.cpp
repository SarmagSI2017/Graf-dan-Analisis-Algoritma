#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
	//t case, n = batasan, x = produksi per hari
	int t,n,x,i,j;
	//int temp[100];
	int sum=0;
	cin>>t;

	for (i = 1; i <= t; i++)
	{
		cin>>n; //nentuin batasan target
		cin>>x; //jumlah buah per hari
		for(j = 0; j < n; j+=x) {
			sum++;
		}
		// sum = temp[];
		cout<<"Kasus #"<<i<<": "<<sum<<endl;
		sum = 0;
	}

	return 0;
}
