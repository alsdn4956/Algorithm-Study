#include <iostream>
using namespace std;

int main() {

    int N,M,i,j;
    int temp;
    
    cin >> N >> M;

    int arr[N] = {0};
    for (int z=0; z<N; z++) {
        arr[z] = z+1;
    }


    for (int q =0; q<M; q++) {
        cin >> i >> j;
        temp = arr[i-1];
        arr[i-1] = arr[j-1];
        arr[j-1] = temp;
    }
    
    for (int w=0; w<N;w++) {
        cout << arr[w] << " ";
    }


  return 0;  
}