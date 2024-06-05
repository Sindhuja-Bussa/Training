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
                print(n.data,"-->",end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
        else:
            n=self.head
            while(n.ref!=None):
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n=self.head
        while(n!=None):
            if(n.data==x):
                break
            n=n.ref
        if(n==None):
            print("Node is not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node    
    def add_before(self,data,x):
        if(self.head==None):
            print("linked list is empty")
            return
        if(self.head.data==x):
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while(n.ref!=None):
            if(n.ref.data==x):
                break
            n=n.ref
        if(n.ref==None):
            print("Node is not found")
        else:
            new_node=Node(data)
            new_node=n.ref
            n.ref=new_node
    def delete_begin(self):
        if(self.head==None):
            print("linked list is empty")
        else:
            self.head=self.head.ref
    def delete_end(self):
        if(self.head==None):
            print("linked list is empty")
        else:
            n=self.head
            while n.ref.ref!=None:
                n=n.ref
            n.nef=None
    def delete_by_value(self,x):
        if(self.head==None):
            print("linked list is empty")
        if x==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while(n!=None):
            if x==n.ref.data:
                break
            n=n.ref
        if(n==None):
            print("Node is not found")
        else:
            n.ref=n.ref.ref
             
LL=Linkedlist()
LL.add_end(30)
LL.delete_begin()
LL.print()
                
        
        
    
    
    
    
