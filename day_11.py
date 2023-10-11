
#best time to buy and sell stock(Q121)
prices=list(map(int,input().split()))
maxpr=0
buy=prices[0]
for i in range(len(prices)):
    if prices[i]<buy:
        buy=prices[i]
    elif prices[i]-buy>maxpr:
        maxpr=prices[i]-buy
return maxpr

#best time to buy and sell stock(Q122)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit

#sum(Q153)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=[]
        target=0
        for i in range(len(nums)):
            left = i+1
            right=len(nums)-1
            while left<right:
                if (nums[i]+nums[left]+nums[right])==target and ([nums[i],nums[left],nums[right]]) not in l:
                    l.append([nums[i],nums[left],nums[right]])
                if (nums[i]+nums[left]+nums[right])<target:
                    left+=1
                else:
                    right-=1
        return l

#Maximum running time of N computers(Q2141)
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total=sum(batteries)
        while batteries[-1]>total//n:
            total-=batteries[-1]
            batteries.pop()
            n-=1
        return total//n









            
        
