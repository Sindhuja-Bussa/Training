class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def print(self):
        if((self.head)==None):
            print("linked list is empty")
        else:
            n=self.head
            while(n!=None):
                print(n.data)
                n=n.ref
LL=Linkedlist()
LL.print()
                
        
        
    
    
    
    
