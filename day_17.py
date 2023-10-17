'''class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
o1=node(1)
o2=node(2)
o3=node(3)
o1.next=o2
o2.next=o3
print(o1,o1.val,o1.next)
print(o2,o2.val,o2.next)

class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
def insertatbeg(head,data):
    pass
l=[2,4,6,8,9]
head=node(l[0])

class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
def insertatbeg(head,data):
    pass


#insertion at end
class node:
    def _init_(self,val=0): #constructor
        self.val=val
        self.next=None
class sll:
    def _init_(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:#creating 1st node
            self.head=node(data)
        else:
           curr=self.head
           while(curr.next):
               curr=curr.next
           new=node(data)
           curr.next=new
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.val,end="->")
            temp=temp.next
l=[2,4,6,8,9]
o=sll()
for i in l:
    o.insertatend(i)
o.printing()

# insertion at begining
class node:
    def _init_(self,val=0): #constructor
        self.val=val
        self.next=None
class sll:
    def _init_(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def printing(self):
        temp=self.head
        while(temp.next):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
o=sll()
for i in l:
    o.insertatbeg(i)
o.printing()

#delete at begining
class node:
    def _init_(self,val=0): #constructor
        self.val=val
        self.next=None
class sll:
    def _init_(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:#creating 1st node
            self.head=node(data)
        else:
           curr=self.head
           while(curr.next):
               curr=curr.next
           new=node(data)
           curr.next=new
    def deleteatbeg(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.val
        
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.val,end="->")
            temp=temp.next
l=[2,4,6,8,9]
o=sll()
for i in l:
    o.insertatend(i)
o.printing()
print()
print(o.deleteatbeg())
print()

#linked list(Koushik Sir)
class node:
    def __init__(self,z):
        self.data=z;
        self.next=None
class list:
    def __init__(self):
        self.head=None
    def creat(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
    def add_end(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            temp=node(x)
            curr.next=temp
    def delete_beg(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.data
    def delete_end(self):
        if self.head==None:
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
        return temp.data
    def traversal(self):
        temp=self.head
        while(temp):
            print(temp.data,end="->")
            temp=temp.next
a=list()
a.creat(10)
a.creat(20)
a.creat(30)
a.add_front(70)
a.add_end(25)
a.delete_end()
a.delete_beg()
a.traversal()

#Convert Binary Number in a Linked list to Integer(Q1290)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=""
        curr=head
        while(curr):
            s+=str(curr.val)
            curr=curr.next
        return int(s,2)

#middle of the linked list(Q876)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

#delete the middle node of the linked list(Q2095)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newnode=ListNode()
        newnode.next=head
        slow=newnode
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return newnode.next

#delete the middle node of the linked list
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newnode=ListNode()
        newnode.next=head
        slow=newnode
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return newnode.next'''


'''#doubly linked list
class node:
    def __init__(self,z):
        self.data=z;
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            temp=node(x)
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
    def add_end(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            temp=node(x)
            temp.prev=self.tail
            self.tail.next=temp
            self.tail=temp
    def delete_beg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.head.prev=None
    def delete_end(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=None
    #reversing a doubly linked list
    def reverse(self):
        curr=self.head
        while curr:
             curr.prev,curr.next=curr.next,curr.prev
             curr=curr.prev
        self.head,self.tail=self.tail,self.head

    def traversal(self):
        temp=self.head
        while(temp):
            print(temp.data,end="-->")
            temp=temp.next
a=dll()
a.add_front(10)
a.add_front(20)
a.add_front(30)
a.add_end(40)
a.delete_beg()
a.delete_end()
a.reverse()
a.traversal()

#basic linked list

class node:
    def _init_(self,val=0):
        self.val=val
        self.next=None
o1=node(1)
o2=node(2)
o3=node(3)
o1.next=o2
o2.next=o3
print(o1,o2,o3,sep="\n")

oa=node(10)
oa.next=node(20)#direct creating nodes without creating objects
oa.next.next=node(30)
print(oa.val,oa.next.val,oa.next.next.val)


class node:
    def _init_(self,val=0):
        self.val=val
        self.next=None
class sll:
    def _init_(self):
        self.head=None
    def insertb(self,data):#insert at begin
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    
    def inserte(self,data):#insert at end
        if self.head==None:
            self.head=node(data)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            new=node(data)
            curr.next=new
    def deleteb(self):#delete at beginning
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.val
    def deletee(self):#delete at end
        if self.head==None:
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next

        temp1=temp.next.val
        temp.next=None
        return temp1
    def insertp(self,data,pos):#insert at position
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            temp=self.head
            pos-=1
            while(pos!=1):
                temp=temp.next
                pos-=1
            new.next=temp.next
            temp.next=new
    def deletep(self,pos):#delete at position
        if self.head==None:
            return
        else:
            temp=self.head
            pos-=2
            while(pos!=1):
                temp=temp.next
                pos-=1
            temp1=temp.next.val
            temp.next=temp.next.next
            return temp1
    def print(self):#display
        temp=self.head
        while(temp):
            print(temp.val,end="-->")
            temp=temp.next
        
        
l=[1,2,3,4,5]
l1=[10,20,30,40]
o=sll()
for i in l:
    o.insertb(i)

for j in l1:
    o.inserte(j)
o.print()
print("\n",o.deleteb())
print("\n",o.deletee())
print("\n",o.deletep(4))
pos=int(input())
o.insertp(100,pos)
o.print()
'''
#double linked list
class node :
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertb(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new

    def inserte(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def deleteb(self):
        if self.head==None:
            return
        else:
            temp1=self.head
            self.head=self.head.next
            self.head.prev=None
        return temp1.val
    
    def deletee(self):
        if self.head==None:
            return
        else:
            temp1=self.tail
            self.tail=self.tail.prev
            self.tail.next=None
        return temp1.val

    def print(self):
        temp=self.head
        while(temp):
            print(temp.val,end="-->")
            temp=temp.next

ob=dll()
l=[1,2,3,4,5]
for i in l:
    ob.insertb(i)
    
l1=[100,200,300,400,500]
for j in l1:
    ob.inserte(j)
    
ob.print()
print()
print('delete at beginning:',ob.deleteb())
print('delete at end:',ob.deletee())
ob.print()

#remove linked list elements(Q203)
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        front=ListNode()
        front.next=head
        curr=front
        prev=None
       while(curr!=None):
            if(curr.val==val):
                if(prev!=None):
                    prev.next=prev.next.next
                    curr=prev
                else:
                    prev=None
                    break
            prev=curr
            curr=curr.next
        return front.next
        
        


