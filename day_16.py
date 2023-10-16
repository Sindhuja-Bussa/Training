#Sliding Window Algorithm
'''l=list(map(int,input().split()))
target=int(input())
i=0
j=0
cursum=l[0]
while j<len(l)-1:
    if cursum==target:
        print(i,j,cursum)
        break
    elif cursum>target:
        cursum-=l[i]
        i+=1
    else:
        j+=1
        cursum+=l[j]


#prime algorithm
def SieveOfEratosthenes(num):
    prime=[True]*(num+1)
    p=2
    while(p*p<=num):
        if prime[p]:
            for i in range(p*p,num+1,p):
                prime[i]=False
        p+=1
    for p in range(2,num+1):
        if prime[p]:
            print(p)
num=int(input())
SieveOfEratosthenes(num)'''

#Histogram
l=list(map(int,input().split()))
maxl=max(l)
for i in  range(maxl,0,-1):
    print(f"{i:2d} | ",end="")
    for j in l:
        if j>=i:
            print(" x ",end="")
        else:
            print("   ",end="")
    print()
    
#longest Substring(Q3)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,longestSubstring=0,0
        sw=set()
        for r in range(len(s)):
            while s[r] in sw:
                sw.remove(s[l])
                l+=1
            sw.add(s[r])
            longestSubstring=max(longestSubstring,(r-l+1))
        return longestSubstring
        
    

