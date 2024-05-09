#include<iostream>
using namespace std;

int mcd(int a, int b){
	if(a==b){
		return a;
	}
	else{
		return mcd(a>b ? a-b : a , b>a ? b-a : b);
	}
}

int mcm(int a, int b){
	/*
		mcm = (a*b) / MCD(a,b);
	*/
	return (a*b) / mcd(a,b);
}


int main(){
	int a = 16;
	int b = 28;
	
	cout << "\nMCD => " << mcd(a,b);
	cout << "\nMCM => " << mcm(a,b) << "\n";
	
	return 0;
}
