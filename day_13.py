#letter combinations of a phone number(Q17)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        def backtrack(i,curstr):
            if len(curstr)==len(digits):
                res.append(curstr)
                return
            for c in d[digits[i]]:
                backtrack(i+1,curstr+c)
        if digits:
            backtrack(0,'')
        return res

#Aggresive Cows
#input:n=5
#      k=3
#l=[5 8 6 3 1]
#output:3
def is_valid(n,k,stalls_pos,mid):
    prevcow=stalls_pos[0]
    count=1
    for i in stalls_pos:
        if (i-prevcow)>=mid:
            count+=1
            prevcow=i
    return True if k==count else False
    
    
def solve(n,k,stalls_pos):
    stalls_pos.sort()
    si=0
    li=stalls_pos[-1]-stalls_pos[0]
    res=0
    while si<=li:
        mid=(si+li)//2
        if is_valid(n,k,stalls_pos,mid):
            res=mid
            si=mid+1
        else:
            li=mid-1
    return res
n=int(input())
k=int(input())
stalls_pos=list(map(int,input().split()))
result=solve(n,k,stalls_pos)
print(result)

#oops:

class cse:
    def _init_(self,a):
        self.a=a
        print("welcome",a)
    def fun(s):
        print("hello",s.a)
o=cse(2)
b=cse(5)
#o._init_(4)#constructor can be created with object also 
o.fun()
