#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	int t,n,sum=0;
	int s[5];
    int temp[5];
	int i,j;
	cin>>t;

	for (i = 1; i <= 4; i++)
	{
		cin>>n;
		for (j = 0; j < n; j++)
		{
			cin>>s[j];
			sum+=s[j];
		}
		temp[i] = sum;
      sum = 0;
	}
   system("cls");
   for(i = 1; i <= 4; i++) {
      if (temp[i] <= 16000) {
            cout<<"Case #"<<i<<": 16GB\n";
         }
         else if (temp[i] <= 32000) {
            cout<<"Case #"<<i<<": 32GB\n";
         }
         else if (temp[i] <= 64000) {
            cout<<"Case #"<<i<<": 64GB\n";
         }
         else {
            cout<<"Case #"<<i<<": 128GB\n";
         }
   }
}
