#cyclic linked list
'''class node:
    def __init__(self,z):
        self.data=z;
        self.next=None
        self.prev=None
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            temp=node(x)
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
            self.tail.next=self.head
            self.head.prev=self.tail
    def add_end(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            temp=node(x)
            temp.prev=self.tail
            self.tail.next=temp
            self.tail=temp
            self.tail.next=self.head
            self.head.prev=self.tail
    def delete_beg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.tail.next=self.head
        self.head.prev=self.tail
    def delete_end(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=self.head
        self.head.prev=self.tail
    def reverse(self):
        curr=self.head
        while curr:
            curr.prev,curr.next=curr.next,curr.prev
            curr=curr.prev
        self.head,self.tail=self.tail,self.head
    def traversal(self):
        print(self.head.data,end="-->")
        temp=self.head.next
        while(temp!=self.head):
            print(temp.data,end="-->")
            temp=temp.next
a=cll()
a.add_front(10)
a.add_front(20)
a.add_front(30)
a.add_end(40)
#a.reverse()
a.delete_beg()
a.delete_end()
a.traversal()


#stack and queue
#1.Remove all adjacent elements in string(Q1047)
#Input: s = "abbaca"
#Output: "ca"

from collections import deque
class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=collections.deque()
        for i in s:
            if not st:#if empty,add
                st.append(i)
            elif i==st[-1]:
                st.pop()
            else:
                st.append(i)
        return "".join(st)

#Minimum String Length After Removing Substrings
Input: s = "ABFCACDB"
Output: 2
Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.

from collections import deque
class Solution:
    def minLength(self, s: str) -> int:
        st=deque()
        for i in s:
            if not st:
                st.append(i)
            elif i=='B' and st[-1]=='A':
                st.pop()
            elif i=='D' and st[-1]=='C':
                st.pop()
            else:
                st.append(i)
        return len(st)

#remove stars from a linked list
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        for i in s:
            if i=='*':
                st.pop()
            else:
                st.append(i)
        return "".join(st)

#Valid Parenthesis
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        st=deque()
        for i in s:
            if i=='(' or i=='{' or i=='[':
                st.append(i)
            else:
                if not st:
                    return False
                elif i==']' and st[-1]=='[':
                    st.pop()
                elif i==')' and st[-1]=='(':
                    st.pop()
                elif i=='}' and st[-1]=='{':
                    st.pop()
                else:
                    return False
        if not st:
            return True
        return False

#tree traversals
class node:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
def printing(root):
    if root==None:
        return
    #print(root.val)#preorder
    printing(root.left)
    print(root.val)#inorder
    printing(root.right)
    #print(root.val)#postorder
    
root=node(1)
root.left=node(2)
root.right=node(3)
printing(root)

#binary tree inorder traversal(Q94)

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        return l

#binary tree preorder traversal(Q144)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def preorder(root):
            if root==None:
                return
            l.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return l

#binary tree postorder traversal(Q145)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def postorder(root):
            if root==None:
                return
            postorder(root.left)
            postorder(root.right)
            l.append(root.val)
        postorder(root)
        return l'''


class node:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
def printing(root):
    if root==None:
        return
    print(root.val)#preorder
    printing(root.left)
    #print(root.val) #inorder
    printing(root.right)
    #print(root.val) #postorder
root=node(5)
root.left=node(2)
root.right=node(3)
printing(root)

#bfs
q=[]
q.append(root)
while q:
    a=q.pop(0)
    print(a.val)
    if a.left:
        q.append(a.left)
    if a.right:
        q.append(a.right)




    
