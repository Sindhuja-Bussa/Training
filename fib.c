#include<stdio.h>
main()
{
	long long int i,n,sum=0;
	int f1=0,f2=1;
	printf("enter n value:");
	scanf("%lld",&n);
	printf("%d %d ",f1,f2);
	for(i=0;i<n-2;i++)
	{
		sum=f1+f2;
		printf("%lld ",sum);
		f1=f2;
		f2=sum;
	}
	
}
