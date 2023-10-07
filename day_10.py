'''def bs(l,si,li,key):
    mid=(si+li)//2
    if si>li:
        return -1
    if l[mid]==key:
        return mid
    if l[mid]<key:
        return bs(l,mid+1,li,key)
    if l[mid]>key:
        return bs(l,si,mid-1,key)
l=list(map(int,input().split()))
key=int(input())
k=bs(l,0,len(l)-1,key)
if k==-1:
    print(" not found")
else:
    print(k)

# floor value (if 6 is not in the list then it will print less than that "5")
def bs_floor(l,target):
    si=0
    li=len(l)-1
    floor=-1
    while(si<=li):
        mid=((si+li)//2)
        if l[mid]==target:
            return l[mid]
        elif l[mid]<target:
            floor=l[mid]
            si=mid+1
        else:
            li=mid-1
    return floor
l=list(map(int,input().split()))
target=int(input())
print(bs_floor(l,target))

#ceil(if number is not present in between the list,it will print greater than that" if 3 it print 4")
def bs_ceil(l,target):
    si=0
    li=len(l)-1
    while(si<=li):
        mid=((si+li)//2)
        if l[mid]==target:
            return l[mid]
        elif l[mid]<target:
            si=mid+1
        else:
            ceil=l[mid]
            li=mid-1
    return ceil
l=list(map(int,input().split()))
target=int(input())
print(bs_ceil(l,target))

#square root of number(floor)
n=int(input())
si=0
li=n//2
floor=-1
while si<=li:
    mid=(si+li)//2
    sq=mid*mid
    if sq==n:
        floor=mid
        break
    elif sq<n:
        floor=mid
        si=mid+1
    else:
        li=mid-1
print(floor)'''

#square root of a num(using recursion)
'''def fun_sqrt(n,si,li,floor):
    if n<0:
        return -1
    if n==1:
        return 1
    if si<=li:
        mid=(si+li)//2
        sq=mid*mid
        if sq==n:
            return mid
        elif sq<n:
            floor=mid
            return fun_sqrt(n,mid+1,li,floor)
        else:
            return fun_sqrt(n,si,mid-1,floor)
    return floor
n=int(input())
si=0
li=n//2
floor=-1
print(fun_sqrt(n,si,li,floor))

#floor_recursion_binary search
def bs_floor(l,target,si,li,floor):
    if si<=li:
        mid=(si+li)//2
        if l[mid]==target:
            return l[mid]
        elif l[mid]<target:
            floor=l[mid]
            return bs_floor(l,target,mid+1,li,floor)
        else:
            return bs_floor(l,target,si,mid-1,floor)
    return floor
l=list(map(int,input().split()))
target=int(input())
si=0
li=len(l)-1
floor=-1
print(bs_floor(l,target,si,li,floor))

#ceil_recursion_binary search
def bs_ceil(l,target,si,li,ceil):
    if si<=li:
        mid=(si+li)//2
        if l[mid]==target:
            return l[mid]
        elif l[mid]<target:
            return bs_ceil(l,target,mid+1,li,ceil)
        else:
            ceil=l[mid]
            return bs_ceil(l,target,si,mid-1,ceil)
    return ceil
l=list(map(int,input().split()))
target=int(input())
si=0
li=len(l)-1
ceil=0
print(bs_ceil(l,target,si,li,ceil))

#square root of a num in float
def sqrt_bs(n,epsilon=1e-6):
    if n<0:
        raise ValueError("Cannot compute the square")
    if n<1:
        left,right=n,1
    else:
        left,right=0,n
    while abs(left-right)>epsilon:
        mid=(left+right)/2
        mid_square=mid*mid
        if mid_square < n:
            left=mid
        else:
            right=mid
    return (left+right)/2
n=int(input())
result=sqrt_bs(n)
print(f"the squareroot of {n} is approx is {result}")

#peakmountain index
def peak(l,si,li):
        mid=(si+li)//2
        if l[mid]>l[mid-1] and l[mid]>l[mid+1]:
            return mid
        elif l[mid-1]>l[mid]:
            li=mid
            return peak(l,si,mid)
        else:
            return peak(l,mid+1,li)
l=list(map(int,input().split()))
si=0
li=len(l)-1
print(peak(l,si,li))'''

#two sum
def sum(l,left,right,target):
    if left<right:
        if l[left]+l[right]==target:
            return left,right
        elif l[left]+l[right]<target:
            return sum(l,left+1,right,target)
        else:
            return sum(l,left,right+1,target)
l=list(map(int,input().split()))
target=int(input())
left=0
right=len(l)-1
print(sum(l,left,right,target))

#string has palindrome or not(possible palindromes) #aabaac aabaa
def palin(s):
    def rev(left,right):
        while left>=0 and right<n and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right-1]
res=[]
for i in range(len(s)):
    pal1=rev(i,i)
    if len(pal1)>1:
        res.append(pal1)
    pal2=rev(i,i+1)
    if len(pal2)>1:
        res.append(pal2)
    return res
str=input()
print(palin(str))

        

    



