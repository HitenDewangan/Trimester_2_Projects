/*Given a sorted array. Write functions using binary search to calculate following things:

. lower_bound(x) : index of first element which is greater or equal to x in the given array
. upper_bound(x): index of first element which is greater than x in the given array
. is_present(x): return true if x is present in the array else return false
*/

/*
For example: 
Input:------------------------ 
arr = {1, 2, 4, 4, 5, 6}
key = 4

Output:--------------------------
lowerbound = 2
upperbound = 4
ispresent = True


*/

#include<iostream>
using namespace std;

string isPresent(int arr[], int size, int key){
    int s=0, e=size-1;

    while(s<=e){
        int mid = s+(e-s)/2;

        if(arr[mid]==key){
            return "True";
        }
        else if(arr[mid]<key){
            s = mid+1;
        }
        else{
            e = mid-1;
        }
    }
    return "False";
}

int lowerBound(int arr[], int size, int key){
    int s=0, e=size-1;
    while(s<e){
        int mid = s+(e-s)/2;
        if(arr[mid]<key){
             s= mid+1;
        }
        else{
            e = mid;
        }
    }
    return s;
}

int upperBound(int arr[], int size, int key){
    int s=0, e=size-1;
    while(s<e){
        int mid = s+(e-s)/2;
        if(arr[mid]<=key){
            s=mid+1;
        }
        else{
            e = mid;
        }
    }
    return s;
}

int main(){
    int n;
    cin>>n;

    int A[n];
    for(int i=0; i<n; i++){
        cin>>A[i];
    }

    int key;
    cin>>key;

    cout<<"Lower bound is: "<<lowerBound(A, n, key)<<endl;
    cout<<"Upper bound is: "<<upperBound(A, n, key)<<endl;
    cout<<"is Present : "<<isPresent(A, n, key)<<endl;



}