/*Given two sorted arrays, merge them to get another sorted array

Example Input:
5                #size of first array
2 4 11 17 91     #first array

4                #size of second array
3 7 9 100        #second array

Example Output :
2 3 4 7 9 11 17 91 100
*/

#include<iostream>
using namespace std;

void mergeArray(int A[], int B[], int a, int b){
    int i=0, j=0;
    int C[a+b];
    while(i<a && j<b){
        if(A[i] < B[j]){
            C[i+j] = A[i];
            i++;
        }
        else{
            C[i+j] = B[j];
            j++;
        }
    }

    while (i < a) {
        C[i + j] = A[i];
        i++;
    }

    while (j < b) {
        C[i + j] = B[j];
        j++;
    }
    
    for(int i=0; i<a+b; i++){
        cout<<C[i]<<" ";
    }
}

int main(){
    int a, b;

    cin>>a;
    int arr1[a];
    for(int i=0; i<a; i++){
        cin>>arr1[i];
    }

    cin>>b;
    int arr2[b];
    for(int i=0; i<b; i++){
        cin>>arr2[i];
    }

    mergeArray(arr1, arr2, a, b);
}