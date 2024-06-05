'''class Node:
    def __init__(self,u):
        self.data=u
        self.ref=None
a=Node(10)
b=Node(20)
a.nxt=b
print(a.data,a.ref)
print(b.data,b.ref)'''

'''class Node:
    def __init__(self,u):
        self.data=u
        self.ref=None
head=Node(10)
head.ref=Node(20)
head.ref.ref=Node(30)
print(head.data)
print(head.ref.data)
print(head.ref.ref.data)'''

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def print(self):
        if(self.head==None):
            print("linked list is empty")
        else:
            n=self.head
            while(n!=None):
                print(n.data,end="->")
                n=n.ref
    def sum(self):
        if(self.head==None):
            print("linked list is empty")
        else:
            s=0
            n=self.head
            while(n!=None):
                s=s+n.data
                n=n.ref
            print("\nSUM:",s)
    def add_end(self,data):
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
        else:
            n=self.head
            while(n.ref!=None):
                n=n.ref
            n.ref=new_node
    def add_even(self):
        n=self.head
        s=0
        while(n!=None):
            if(n.data%2==0):
                s=s+n.data
                n=n.ref
        print("\nEVEN SUM:",s)
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def search(self,x):
        n=self.head
        flag=0
        while(n!=None):
            if(n.data==x):
                flag=1
                break
            n=n.ref
        if(flag==1):
            print("found")
        else:
            print("not found")
    def middle_node(self):
        slow_pointer=self.head
        fast_pointer=self.head
        while fast_pointer!=None and fast_pointer.ref!=None:
            fast_pointer=fast_pointer.ref.ref
            slow_pointer=slow_pointer.ref
        print("\nmiddle element:",slow_pointer.data)
    def possible_pairs(self):
        slow_pointer=self.head
        fast_pointer=self.head.ref
        while(slow_pointer.ref!=None):
            while(fast_pointer!=None):
                print(slow_pointer.data,",",fast_pointer.data)
                fast_pointer=fast_pointer.ref
            slow_pointer=slow_pointer.ref
            fast_pointer=slow_pointer.ref
    def eor(self):
        fast_pointer=self.head
        slow_pointer=self.head
        while(fast_pointer!=None and fast_pointer.ref!=None):
            slow_pointer=slow_pointer.ref
            fast_pointer=fast_pointer.ref.ref
        if(fast_pointer==None):
            print('even')
        else:
            print('odd')
    def sequence_count(self):
        n=self.head
        count=1
        max=0
        while(n.ref!=None):
            if(n.data+1==n.ref.data):
                count=count+1
            else:
                if(count>max):
                    max=count
                count=1
            n=n.ref
        if(count>max):
            max=count
        print(max)
    def selection_sort(self):
        t1=self.head
        t2=self.head.ref
        while(t1.ref!=None):
            t2=t1.ref
            while(t2!=None):
                if(t1.data>t2.data):
                    t=Node(t1.data)
                    t1.data=t2.data
                    t2.data=t.data
                t2=t2.ref
            t1=t1.ref
        self.print()
    def bubble_sort(self): 
        N=self.head
        while(N!=None):
            n=self.head
            while(n.ref!=None):
                if(n.data>n.ref.data):
                    n.data=n.ref.data
                    n.ref.data=n.data
            N=N.ref
        self.print()
    def bubble_bestcase(self):
        c=0
        N=self.head
        p=None
        while(N.ref!=None):
            f=0
            n=self.head
            while(n.ref!=p):
                if(n.data>n.ref.data):
                    f=1
                    n.data,n.ref.data=n.ref.data,n.data
                n=n.ref
                c=c+1
            if(f==0):
                break
            return c
            p=n
            N=N.ref
        
        self.print()
    def swap_3(self):
        t1=self.head
        t2=self.head.ref
        t3=self.head.ref.ref
        while(t1.ref!=None):
            if(t1.ref==None):
                    `ArithmeticError                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            t1.ref=t3.data
            t3.ref=t2.data
            t2.ref=t1.data
        t=t.ref
        
LL=Linkedlist()
'''LL2=Linkedlist()
LL2.add_end(30)'''
LL.add_begin(9)
LL.add_begin(7)
LL.add_begin(6)
LL.add_begin(4)
LL.add_begin(2)
LL.add_begin(3)
LL.add_begin(1)
LL.add_begin(0)
LL.sum()
LL.search(20)
LL.search(30)
LL.print()
LL.middle_node()
LL.possible_pairs()
LL.eor()
LL.sequence_count()
LL.selection_sort()
print() 
LL.bubble_bestcase()
