#include<stdio.h>
main()
{
	char str[10],rev[10];
	int i,j=0,l=0;
	gets(str);
	for(i=0;str[i]!='\0';i++)
	{
		l++;
	}
	if((str[i]>=65 && str[i]<=90) || (str[i]>=97 && str[i]<=122))
	{
	for(i=(l-1);i>=0;i--)
	{
		rev[j]=str[i];
		j++;
	}
	rev[j]='\0';
	puts(rev);
    }
    else if((str[i]>=32 && str[i]<=47) || (str[i]>=58 && str[i]<=64) || (str[i]>=91 && str[i]<=96) || (str[i]>=123 && str[i]<=126))
    {
    	for(i=0;i<l;i++)
	   {
	   	  str[j]=str[i];
	   	  j++;
	   }
	   str[j]='\0';
	   puts(str);
	}
}
