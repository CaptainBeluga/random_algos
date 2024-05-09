#include<iostream>
using namespace std;


int fact(int n){
	if(n>1){
		return n* fact(n-1);
	}
	else{
		return 1;
	}
}

int main(){
	cout << "\nFACT => " << fact(5);
	
	return 0;
}
