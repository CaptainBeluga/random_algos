#include<iostream>

using namespace std;

int beluga_sort(int a[], int arr[],int len){	
	int ll=0;
	
	for(int f=0;f<len;f++){
		a[ll] = arr[f];
		ll++;
		
		//sorting
		int max = a[0];

		for(int i=0; i<ll; i++){
			if(max < arr[f]){
				max = a[i];
			}
			
			else{
				i = i-1 < 0 ? 1 : i;
				
				if(max==arr[f]){
					ll-= ll > 1 ? 1 : 0;
				}
				
				else{
					//SHR FUNCTION
					for(int k=ll-1; k >= i-1;k--){
						a[k+1] = a[k];
			
					}
					a[i-1] = arr[f];
				}
	
				break;
			}
		}	
		
	}
	
	return ll;
	
	
	
}

void print_array(int a[],int ll){
	cout << "\nSORTED ARRAY ";
	for(int i = 0; i < ll; i++) {
		 cout << "  |  " << a[i];		
	}
	
	cout << "\n\n\n";
}
int main(){
	int arr[] = {-23,15,0,1,22,45,32};
	int a[999];
	
	/*
		arr => data array
		a => sorted array 
	*/
	
	int ll = beluga_sort(a,arr,sizeof(arr) / sizeof(arr[0]));
	
	print_array(a,ll);
}
