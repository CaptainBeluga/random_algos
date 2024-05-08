#include<iostream>
using namespace std;

//pos to delete (LEFT SHIFT)
void shl(int arr[],int &ll,int pos){
	for(int i=pos; i <ll-1;i++){
		arr[i] = arr[i+1];
	}
	ll--;
}

//pos where to store the new `value` and start the RIGHT SHIFT
void shr(int arr[],int &ll, int pos,int value){
	for(int i=ll-1; i >= pos;i--){
		arr[i+1] = arr[i];
			
	}
	arr[pos] = value;
	ll++;
}


int main(){
	int arr[] = {1,2,4,4,5};
	int ll = sizeof(arr) / sizeof(arr[0]);

	shr(arr,ll,2,3);
	shl(arr,ll,2);
}
