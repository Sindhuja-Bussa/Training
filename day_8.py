#quick sort

'''def qsorting(l,start,end):
    pi=l[end]
    i=start-1
    for j in range(start,end):
        if l[j]<pi:
            i=i+1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[end]=l[end],l[i+1]
    return i+1

def quick(l,start,end):
    if start<end:
        pi=qsorting(l,start,end)
        quick(l,start,pi-1)
        quick(l,pi+1,end)
l=list(map(int,input().split()))
quick(l,0,len(l)-1)
print(l)
print(*l)

#merge_sort with inversion
def mergesort(l,inversion):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        li=mergesort(left,inversion)
        ri=mergesort(right,inversion)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                l[k]=left[i]
                i+=1
                k+=1
            else:
                l[k]=right[j]
                j+=1
                k+=1
                inversion+=len(left)-i
        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1
        return li+ri+inversion
    return 0
n=int(input())
l=[]
for i in range(n):
   l.append(list(map(int,input().split())))
print('inversion count',mergesort(l,0))
print(l)




#merge sort
def mergesort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        left=mergesort(left)
        right=mergesort(right)
        li=merge(left,right)
        return li
    return l
def merge(left,right):
    res=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

l=list(map(int,input().split()))
print(mergesort(l))
    
#merge sort with one function

def mergesort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                l[k]=left[i]
                i+=1
                k+=1

            else:
                l[k]=right[j]
                j+=1
                k+=1

        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1
        #return li+ri+inversion
    #return 0
l=list(map(int,input().split()))
mergesort(l)
print(l)

#inversion merge sort

def mergesort(l,inversion):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        li=mergesort(left,inversion)
        ri=mergesort(right,inversion)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                l[k]=left[i]
                i+=1
                k+=1

            else:
                l[k]=right[j]
                j+=1
                k+=1
                inversion+=len(left)-i

        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1
        return li+ri+inversion
    return 0
l=list(map(int,input().split()))
print(mergesort(l,0))
print(l)

#sudoku solver
def solve(s):
    if s==81:
        return board
    row=s//9
    col=s%9
    if board[row][col]!=".":
        solve(s+1)
    for i in "123456789":
        if isvalid(i,row,col):
            board[row][col]=i
            solve(s+1)
        board[row][col]!="."
def isvalid(c,row,col):
    for i in range(9):
        if board[i][col]==c or board[row][i]==c or board[3*(row//3)+i//3][3*(col//3)+(i%3)]==c:
            return False
        return True

#all possible subsets equal to sum

def fun(l,target):
    def backtrack(start,sum,subset):
        if sum==target:
            res.append(subset[:])
            return
        if sum>target or start==len(l):
            return
        subset.append(l[start])
        backtrack(start+1,sum+l[start],subset)
        subset.pop()
        backtrack(start+1,sum,subset)

    res=[]
    backtrack(0,0,[])
    return res
l=list(map(int,input().split()))
target=int(input())
result=fun(l,target)
if result:
    print(result)
else:
    print("No subsets with sum")'''


        
        



