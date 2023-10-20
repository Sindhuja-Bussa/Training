#dfs
def dfs(start,vis):
    vis.add(start)
    for i in d[start]:
        if i not in res:
            dfs(i,res)

#All Paths From Source to Target(Q797)
 class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        def dfs(start,end,visited):
            if start==end:
                val=visited+[start]
                ans.append(val)
                return
            visited.append(start)
            for i in graph[start]:
                if i not in visited:
                    dfs(i,end,visited)
            visited.pop()
        dfs(0,len(graph)-1,[])
        return ans

#cycle is present or not(dfs)
def dfs(start,vis):
    vis.add(start)
    for i in d[start]:
        if i in res:
            return True
        else:
            if dfs(i,vis):
                return True
for i in d:
    if dfs(i,[]):
        return True

#Course Schedule(Q207)
class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        d={i:[] for i in range(n)}
        for i in p:
            d[i[0]].append(i[1])
        print(d)
        def dfs(start,vis):
            if start in vis:
                return False
            if d[start]==[]:
                return True
            vis.append(start)
            for i in d[start]:
                if dfs(i,vis)==False:
                    return False
            vis.remove(start)
            d[start]=[]
            return True
        for i in d:
            if dfs(i,[])==False:
                return False
        return True
#Cheapest Flights with k stops
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("inf")]*n
        prices[src]=0
        for i in range(k+1):
            temp=prices.copy()
            for s,d,w in flights:
                if prices[s]!=float("inf") and prices[s]+w<temp[d]:
                    temp[d]=prices[s]+w
            prices=temp
        return -1 if prices[dst]==float("inf") else prices[dst]

#keys and rooms(Q841)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis=set()
        def dfs(start):
            vis.add(start)
            for i in rooms[start]:
                if i not in vis:
                    dfs(i)
        dfs(0)
        return True if len(vis)==len(rooms) else False

        
        


       
