#Rotate Array(189)
'''ip: [2, 3, 4, 5, 6]
     k=2
op: [5, 6, 2, 3, 4]'''
'''l=list(map(int,input().split(', ')))
k=int(input())
for i in range(k):
    l.insert(0,l.pop())
print(l)

#method 2

l=list(map(int,input().split(', ')))
n=len(l)
k=int(input())
for i in range(k):
    temp=l[-1]
    for j in range(n-1,0,-1):
        l[j]=l[j-1]
    l[0]=temp
print(l)

#slicing
l=list(map(int,input().split(', ')))
k=int(input())
if k>=len(l):
    k=k%len(l)
a=len(l)-k
l[:]=l[a:]+l[:a]
print(l)


#Rotate Array(Add at Back)
ip: [2, 3, 4, 5, 6]
     k=2
op: [4, 5, 6, 2, 3]
l=list(map(int,input().split(', ')))
k=int(input())
for i in range(k):
    l.append(l.pop(0))
print(l)'''


#slicing
l=list(map(int,input().split(', ')))
k=int(input())
a=k
l[:]=l[a:]+l[:a]
print(l)

#using temp variable
'''l=list(map(int,input().split(', ')))
k=int(input())
for i in range(k):
    temp=l[0]
    for j in range(len(l)-1):
        l[j]=l[j+1]
    l[-1]=temp
print(l)'''

#search element in rotated array(Q33)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        si=0
        li=len(nums)-1
        while si<=li:
            mid=(si+li)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[si]:
                if target>=nums[si] and target<=nums[mid]:
                    si=mid+1
                else:
                    li=mid-1
       return -1

#knapsack
def knapsack(W,wt,val,n):
    dp = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]
val = list(map(int,input().split()))
wt = list(map(int,input().split()))
W = int(input())
n = len(val)
print(knapsack(W,wt,val,n))

#coin change(Q322)

coins=list(map(int,input().split(', ')))
amount=int(input())
for i in range(len(coins)+1):
    for j in range(amount+1):
        if coins[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=min(1+dp[i][j-coins[i+1]]),dp[i-1][j]
print


    
        







