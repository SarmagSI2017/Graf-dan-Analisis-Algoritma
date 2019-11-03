#include<iostream>
#include<string>
#include<cstring>
using namespace std;

int main(){
	int a;
	int x = 0;
	int y = 0;
	string s;
	
//	Input String
	getline(cin, s);
	
//	String to Array
	a = s.size() - 1;
	char cs[a];
	strcpy(cs, s.c_str());
	for(int i=0;i<=a;i++){
		if(cs[i] == 'N'){
			y++;
		}else if(cs[i] == 'S'){
			y--;
		}else if(cs[i] == 'E'){
			x++;
		}else{
//			West
			x--;
		}
	}
	if(x < 0)
		x = x * -1;
	if(y < 0)
		y = y * -1;
		
	cout<<x+y;
	return 0;
}
