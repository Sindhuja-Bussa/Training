#sort colors
def sortColors(nums):
        l=0
        i=0
        r=len(nums)-1
        while i<=r:
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
                i+=1
            elif nums[i]==1:
                i+=1
            elif nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
        return nums
nums=list(map(int,input().split()))
print(sortcolors(nums))

#Rain Trapping(Q42)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return True
        l=0
        r=len(height)-1
        maxl=height[l]
        maxr=height[r]
        res=0
        while l<r:
            if maxl<maxr:
                l+=1
                maxl=max(maxl,height[l])
                res+=(maxl-height[l])
            else:
                r-=1
                maxr=max(maxr,height[r])
                res+=(maxr-height[r])
        return res

#Unique Morse Code Words(Q804)
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d={}
        s="abcdefghijklmnopqrstuvwxyz"
        m=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        b=[]
        for i in range(len(s)):
            d[s[i]]=m[i]
        for i in range(len(words)):
            res=""
            w=words[i]
            for j in range(len(w)):
                res+=d[w[j]]
            if res not in b:
                b.append(res)
        return len(b)

