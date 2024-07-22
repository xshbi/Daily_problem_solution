"This question related to arrays and here we have to find the peak element which is not smaller than its neighbours."
"we are here doing binary search and calculate mid val"
"Else if arr[mid-1]>arr[mid]".
"Else if arr[mid]< arr[mid+1]"

"arr = [1,3,20,4,1,0]
start = 0 ,end= 5"

#include<iostream>
using namespace std;

int findPeakelement(int arr[],int low,int high,int n){
  int mid = low+(high-low)/2;


  if((mid == 0 || arr[mid - 1] <= arr[mid]) && (mid == n-1|| arr[mid+1] <= arr[mid])){
    return mid;
  }


  else if (mid >0 && arr[mid-1] > arr[mid]) {
    return findpeakelement(arr,low,mid-1,n);
  }
}


else {
  return findpeakelement(arr,mid+1,high,n);
}


int main(){


  int arr[] = {0,6,8,5,7,9};
  int n = 6;



  cout<<"peak element index:"<< findPeakelement(arr,0,n-1,n)<<endl;
return 0;
}
