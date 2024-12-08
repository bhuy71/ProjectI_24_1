#include <stdio.h>
#include <string.h>
int find_min(int arr[],int n){
	int min =10000;
	for(int i=0;i<n;i++){
		if(min>arr[i]){
			min=arr[i];
			}
	}
	return min;
}
int find_max(int arr[],int n){
	int max =-10000;
	for(int i=0;i<n;i++){
		if(max<arr[i]){
			max=arr[i];
			}
	}
	return max;
}
int sum(int arr[],int n){
	int sum=0;
	for(int i=0;i<n;i++){
		sum+=arr[i];
	}
	return sum;
}
int find_max_segment(int arr[],int a,int b){
	int max=-10000;
	for(int i=a;i<=b;i++){
		if(max<arr[i]){
			max=arr[i];
			}
	}
	return max;
}

int main(){
	int n;
	int result[10000];
	scanf("%d",&n);
	int arr[n];
	for(int i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	
	char query[50];
	int i=0;
	
	while (1){
		scanf("%s",&query);
		if(strcmp(query,"*")==0){
			continue;
		}
		if(strcmp(query,"***")==0){
			break;
		}
		if(strcmp(query,"find-max")==0){
			result[i]=find_max(arr,n);
			i++;
		}else if(strcmp(query,"find-min")==0){
			result[i]=find_min(arr,n);
			i++;
		}else if(strcmp(query,"sum")==0){
			result[i]=sum(arr,n);
			i++;
		}else if(strncmp(query,"find-max-segment",16)==0){
			int a,b;
			scanf("%d %d",&a ,&b);
			result[i]=find_max_segment(arr,a-1,b-1);
			i++;
		}
	}
	for(int j=0;j<i;j++){
		printf("%d \n",result[j]);
	}
	return 0;
}
