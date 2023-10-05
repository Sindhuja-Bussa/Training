#include<stdio.h>
main()
{
	short n,m,i,j,rsum=0,rcount1=0,csum=0,rcount0=0,ccount0=0,ccount1=0,dsum=0,dcount0=0,dcount1=0,rdsum=0,rdcount1=0,rdcount0=0;
	scanf("%hi %hi",&n,&m);
	int arr[100][100];
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			scanf("%d",&arr[i][j]);	
		}
	}
	for(i=0;i<n;i++)
	{
		rsum=0;
		for(j=0;j<m;j++)
		{
			rsum=rsum+arr[i][j];	
		}
		if((rsum==4))
		{
			rcount1++;	
		}
		else if(rsum==0)
		{
			rcount0++;
		}
    }
	printf("1's horizontal count: %hi\n",rcount1);
	printf("0's horizontal count: %hi\n",rcount0);
	for(j=0;j<m;j++)
	{
		csum=0;
		for(i=0;i<n;i++)
		{
			csum=csum+arr[i][j];
		}
		if((csum==4))
		{
			ccount1++;	
		}
		else if(csum==0)
		{
			ccount0++;
		}
	}
	printf("1's vertical count: %hi\n",ccount0);
	printf("0's vertical count: %hi\n",ccount1);
    dsum=0;
    for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			if(i==j)
			dsum=dsum+arr[i][j];
		    	
		}
		if((dsum==4))
		{
			dcount1++;	
		}
		else if(dsum==0)
		{
			dcount0++;
		}
	}
	printf("1's left diag count: %hi\n",dcount1);
	printf("0's left diag count: %hi\n",dcount0);
	rdsum=0;
    for(i=n-1;i>=0;i--)
	{
		rdsum=rdsum+arr[m-i-1][i];	    	
    }
	if((rdsum==4))
	{
		rdcount1++;	
	}
	else if(rdsum==0)
	{
		rdcount0++;
	}
	printf("1's right diag count: %hi\n",rdcount1);
	printf("0's right diag count: %hi\n",rdcount0);
}
