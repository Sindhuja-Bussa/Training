#random number

'''import random
a=input('How idiot are you? - ')
print(random.randint(1,100),'%')

#table
def fun(n,i):
    if i==0:
        return
    fun(n,i-1)
    print(n,"x",i,"=",(n*i))
n=int(input())
i=int(input())
fun(n,i)

#palindrome
s=input()
h=s[::-1]
print(h)
if h==s:
    print("palindrome")
else:
    print("not a palindrome")

#length of a string
s=input()
count=0
for i in s:
    count=count+1
print(count)

#palindrome
s=input()
i=0
j=len(s)-1
while i<=j:
    if(s[i]!=s[j]):
        print("no")
        break
    i+=1
    j-=1
else:
    print("yes")

#palindrome using recursion
def fun(s,i,j):
    if i>j:
        return True
    if s[i]!=s[j]:
        return False
    return fun(s,i+1,j-1)
s=input()
print(fun(s,0,len(s)-1))'''


#0 1 0 1
#1 1 0 0
#0 0 1 0
#0 0 1 1


def fun(l,i,j,n):
    if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]=0
    if i<n-1:
        fun(l,i+1,j,n)
    if i>0:
        fun(l,i-1,j,n)
    if j<n-1:
        fun(l,i,j+1,n)
    if j>0:
        fun(l,i,j-1,n)
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
count=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count=count+1
            fun(l,i,j,n)
print(count)

    
    



    
            
