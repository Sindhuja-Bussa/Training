#odd or even

#include <stdio.h>
int main() {
    // Write C code here
    int a;
    scanf("%d",a);
    if(a&1==1)
    printf("odd");
    else
    printf("even");

    return 0;
}

#conversion of decimal to binary
int a[100],n,i=0;
   scanf("%d",&n);
   while(n>0)
   {
       a[i]=n%2;
       n=n/2;
       i++;
   }
   for(i=i-1;i>=0;i--)
   {
       printf("%d",a[i]);
   }
   
   

   /* int a=15;
   printf("%d",a | a+1);*/
   
   
#smallest number greater than n,with exactly onebit diff from binary form
   
   int a,i;
   scanf("%d",&a);
   scanf("%d",&i);
   if(a&(1<<(i-1)))
   {
       printf("yes");
   }
   else
   {
       printf("no");
   }
   

#decimal to binary

#include<stdio.h>
main()
{

int a[100],n,i=0;
   scanf("%d",&n);
   while(n>0)
   {
       a[i]=n%2;
       n=n/2;
       i++;
   }
   for(i=i-1;i>=0;i--)
   {
       printf("%d",a[i]);
   }
}

#power of 2
int count=0,n=256;
while(n)
{
	count++;
	n=n&(n-1);
}
if(count==1)
printf("true");
else
printf("false");





#power of 2


n=int(input())
s=[]
while(n>0):
    x=n%2
    n=n//2
    s.append(x)
s.reverse()
count=0
for i in s:
    if(i==1):
        count=count+1
if(count==1):
    printf("yes")
else:
    printf("no")
    
    
#power of 4

n=int(input())
s=[]
while(n>0):
    x=n%2
    n=n//2
    s.append(x)
s.reverse()
count=0
count1=0
for i in s:
    if(i==1):
        count=count+1
    else:
    	count1=count1+1
if(count==1 and count1&1==0):
    printf("yes")
else:
    printf("no")
    
toggle
n=int(input())
k=int(input())
s=[]
while(n>0):
    x=n%2
    n=n//2
    s.append(x)
s.reverse()
print(s)
if(s[k]==0):
	s[k]=1
elif(s[k]==1):
	s[k]=0
print(s)	
sum=0
l=len(s)
m=l-1
for i in s:
	a=(2**m)*i
	su=su+a
	m=m-1
print(sum)


#factorial

#include <stdio.h>
long long int factorial(long long int);
long long int n,z;
int main()
{
    scanf("%lld",&n);
    z=factorial(n);
    printf("%lld",z);
    return 0;
}
long long int factorial(long long int n)
{
    if(n==0 || n==1)
    return 1;
    else
    return n*factorial(n-1);
}


#fibbonacci

#include <stdio.h>
int fib(int);
int n,i;
int main()
{
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
    printf("%d ",fib(i));
    }
    return 0;
}
int fib(int n)
{
    if(n==0 || n==1)
    return n;
    else
    return fib(n-1)+fib(n-2);
}
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
    
