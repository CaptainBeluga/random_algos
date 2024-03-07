#include<iostream>
using namespace std;

int ask(string msg) {
	int choice;
	cout << msg;
	cin >> choice;

	return choice;

}

void print_array(int a[],int ll){
	cout << "\nARRAY ";
	for(int i = 0; i < ll; i++) {
		 cout << "  |  " << a[i];		
	}
	
	cout << "\n\n\n";
}

void array_add(int a[], int &ll, int val){
	a[ll] = val;
	ll++;
}

void shr(int a[],int &ll,int pos,int x){
	for(int i=ll-1; i >= pos;i--){
		a[i+1] = a[i];
		
	}
	
	a[pos] = x;
}

void sort(int a[], int &ll,int val){
	int max = a[0];

	for(int i=0; i<ll; i++){
		if(max < val){
			max = a[i];
		}
		
		else{
			i = i-1 < 0 ? 1 : i;
			
			if(max==val){
				ll-= ll > 1 ? 1 : 0
			}
			
			else{
				shr(a,ll, i-1,val);
			}

			break;
		}
	}
}



int main(){

	const int len = 999;
	int ll = 0;
	
	int a[len];
	
	while(true){
		if(ll < len){
			int f = ask("\nVALUE => ");
			array_add(a,ll,f);
			
			sort(a,ll,f);
			print_array(a,ll);
		}
		
		else{
			cout << "\n\n[X] ARRAY FULL !!!\n\n";
			break;
		}

	}
	
	system("pause");
	return 0;
}
