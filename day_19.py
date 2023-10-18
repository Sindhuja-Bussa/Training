#Search in a Binary Tree(Q700)
Find the node in the BST that the node's value equals val and return the subtree rooted
with that node. If such a node does not exist, return null.

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return
        if root.val==val:
            return root
        elif root.val>val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)

#Convert Sorted Array to Binary Search Tree(Q108)
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def fun(si,li):
            if si<=li:
                mid=(si+li)//2
                root=TreeNode(nums[mid])
                root.left=fun(si,mid-1)
                root.right=fun(mid+1,li)
                return root
        return fun(0,len(nums)-1)
        
#Insert into a Binary Search Tree(Q701)
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            root=TreeNode(val)
            return root
        if val>root.val:
            root.right=self.insertIntoBST(root.right,val)
        else:
            root.left=self.insertIntoBST(root.left,val)

        return root

#Maximum depth of a binary search tree(Q104)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1


#Minimum depth of a binary search tree(Q111)
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        if root.right==None:
            return self.minDepth(root.left)+1
        if root.left==None:
            return self.minDepth(root.right)+1
        left=self.minDepth(root.left)
        right=self.minDepth(root.right)
        return min(left,right)+1

#Find If Path Exists in Graph(Q1971)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True
        d={i:[] for i in range(n)}
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        q=[source]
        vis=set()
        while q:
            a=q.pop()
            for i in d[a]:
                if i==destination:
                    return True
                if i not in vis:
                    q.append(i)
                    vis.add(i)
        return False

#Find Centre of Star Graph(Q1791)
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]



