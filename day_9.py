#counting sort

'''l=list(map(int,input().split()))
count=[0 for i in range(10)]
for i in range(len(l)):
    count[l[i]]+=1#2 how many times is present
    #value will be 8 count(8) at 8 we are going place it
for i in range(1,len(count)):
    count[i]+=count[i-1]
res=[0]*len(l)#size of resultant
for i in range(len(l)):
    res[count[l[i]]-1]=l[i]
    count[l[i]]-=1
print(res)

#for loop
a=range(1,10,2)
print(a,type(a))
print(list(a),type(a))

def fun(a):
    return str(a)
l=[1,2,3,4]
l=list(map(fun,l))
print(l)

def fun(a):
    return str(a)
l=[[1,2,3],[4,5,6],[7,8,9]]
l=list(map(fun,l))
print(l)

def fun(a):
    return sum(a)
l=[[1,2,3],[4,5,6],[7,8,9]]
l=list(map(fun,l))
print(l)


def fun(a):
    return sum(a)
l=[[1,2,3],[4,5,6],[7,8,9]]
l=list(map(lambda a:max(a),l))
print(l)

def fun(a):
    return sum(a)
l=[[1,2,3],[4,5,6],[7,8,9]]
l=list(map(lambda a:a.sort(),l))
print(l)

def fun(a):
    return sum(a)
l=[[1,2,3],[4,5,6],[7,9,8]]
l=list(map(lambda a:sorted(a),l))
print(l)

def fun(a):
    return sum(a)
l=[[1,3,2],[8,6,7],[9,0,0]]
a=[2,3,4,5,6]
l=list(filter(lambda a:a%2==0,a))
print(l)

#sorted acc to sum of individual set
def fun(a):
    return sum(a)
l=[[1,3,2],[8,6,7],[9,0,0]]
l.sort(key=sum)
print(l)

def fun(a):
    return sum(a)
l=[[1,3,2],[8,6,7],[9,0,0]]
l.sort(key=lambda x:x[0]+x[1])
print(l)

#enumerate and zip
def fun(a):
    return sum(a)
l=[[1,3,2],[8,6,7],[9,0,0]]
print(max(l,key=lambda x:x[0]+x[1]))
print(l)

a=[1,2,3,4,5]
b=[5,6,7,8,9]
print(zip(a,b))
print(list(zip(a,b)))
print(enumerate(a))
print(list(enumerate(a)))
for i in enumerate(a):
    print(i)
for i,j in enumerate(a):
    print(i)
for i,j in enumerate(a):
    print(i,j)
for i in [range(1,10),range(10,1,-1),range(0,20,2)]:
    print(i)
for i in [range(1,10),range(10,1,-1),range(0,20,2)]:
    print(list(i))
    
#binary search
def bs(l,si,li,key):
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

#sum of array elements_recursion_divide and conquer

def sum(l,si,li):
    if si==li:
        return l[si]
    if si>li:
        return -1
    mid=(si+li)//2
    return sum(l,si,mid)+sum(l,mid+1,li)
l=list(map(int,input().split()))
res=sum(l,0,len(l)-1)
print(res)'''

#max element
def sum(l,si,li):
    if si==li:
        return l[si]
    if si>li:
        return -1
    mid=(si+li)//2
    return max(sum(l,si,mid),sum(l,mid+1,li))
l=list(map(int,input().split()))
res=sum(l,0,len(l)-1)
print(res)

