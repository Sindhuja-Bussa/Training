'''#print the alphabet using ascii
a=68
print(chr(a))

#ip:B  op:2
#lowercase
a=input("enter a string:")
print(ord(a)-96)

#uppercase
a=input("enter a string:")
print(ord(a)-64)

#uppercase and lowercase
a=input("enter a string:")
if(ord(a)>96):
    print(ord(a)-96)
else:
    print(ord(a)-64)

#ip: h and 3
    #op: k
a=input("enter a string:")
k=int(input("enter the pos:"))
print(chr(ord(a)+k))

#ip: x and 4
#op:b
a=input("enter a string:")
k=int(input("enter the pos:"))
if((ord(a)+k)>122):
    print(chr((ord(a)+k)-26))
else:
    print(chr(ord(a)+k))


#ip:4
#op:  *
   #  * *
   #  * * *
   #  * * * *
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

#ip:4
#op:   *
   #  *  *
   # *  *  *
   #*  *  *  *
n=int(input())
for i in range(n):
    for j in range(n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
    OR
n=int(input())
for i in range(n):
    print(" "*(n-i) + "* " *(i+1))
#inverted pyramid
n=int(input())
for i in range(n):
    print(" "*(i+1) + "* " *(n-i))
    
#inverted diamond
n=int(input())
for i in range(n):
    print(" "*(n-i) + "* " *(i+1))
for i in range(n):
    print(" "*(i+1) + "* " *(n-i))

#ip:4
#op:  1
#     2 2
 #    3 3 3
  #   4 4 4 4
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(j,end=" ")
    print()

or
n=int(input())
for i in range(n):
    print(str(i+1)*(i+1))


n=int(input())
b=1
for i in range(1,n+1):
    print(b*i)
    b=(b*10)+1

1000%9=111.1
100%9=11.1
10%9=1.1
#print((10**i)) 1 10 100 10000
#print((10**i)//9) 1 11 111 1111

n=int(input())
for i in range(1,n+1): 
    print(((10**i)//9)*i)'''

class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class add_back(self,x):
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
class add_front(self,x):
    def __init__(self):
        self.head=None
    def creat(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
class display(self,x):
    def dis(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next
b=cse()
b.creat(20)
b.creat(30)
b.add_front(60)
b.creat(40)
c.creat(500)
c.add_front(50)
c.display()
        




    
    


