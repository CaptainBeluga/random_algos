#include<iostream>
using namespace std;

int mcdRecursive(int a, int b){
	if(a==b){
		return a;
	}
	else{
		return mcdRecursive(a>b ? a-b : a , b>a ? b-a : b);
	}
}

int mcdNormal(int a, int b){
	while(a!=b){
		
		a = a>b ? a-b : a;
		b = b>a ? b-a : b;
		
		/*
		if(a > b){
			a = a-b;
		}
		else{
			b = b-a;
		}
		*/
	}	
}

int mcdModuloRecursive(int a,int b){
	if(a%b==0){
		return b;
	}
	
	else{
		int c = a%b;
		return mcdModuloRecursive(b,c);
	}
}

int mcdModulo(int a,int b){
	while(a%b!=0){
		int c = a%b;
		a = b;
		b = c;
	}
	
	return b;
}

int main(){
	int a = 12;
	int b = 16;
		
	// FASTER
	cout << "\nMCD RECURSIVE => " << mcdRecursive(a,b) << "\n\n"; 
	cout << "\nMDC NORMAL => " << mcdNormal(a,b) << "\n\n";


	cout << "\nMDC MODULO RECURSIVE => " << mcdModuloRecursive(a,b) << "\n\n";
	cout << "\nMDC MODULO => " << mcdModulo(a,b) << "\n\n";
	
	return 0;	
}
