'''#inheritance
#single
class cse():
    def fun1(self):
        print("one")
    def fun2(self):
        print("two")
class two(cse):
    def fun3(self):
        print("three")
    def fun4(self):
        print("four")
a=two()
a.fun3()
a.fun1()

#mutliple
class cse():
    def fun1(self):
        print("bhavana")
    def fun2(self):
        print("sindhuja")
class two(cse):
    def fun3(self):
        print("pragnya")
    def fun4(self):
        print("sathwika")
class three(two):
    def fun5(self):
        print("srija")
    def fun6(self):
        print("umesh")
o=cse()
a=two()
b=three()
b.fun5()
b.fun3()
b.fun1()

#polymorphism
class cse():
    def fun1(self):
        print("one")
    def fun1(self):
        print("two")
class two(cse):
    def fun3(self):
        print("three")
    def fun4(self):
        print("four")
o=cse()
o.fun1()

#super
class cse():
    def fun1(self):
        print("one")
    def fun2(self):
        print("two")
class two(cse):
    def fun3(self):
        super().fun1()
        print("three")
    def fun4(self):
        super().fun2()
        print("four")
a=two()
a.fun3()
a.fun4()

class cse():
    def fun1(self):
        print("one")
    def fun2(self):
        print("two")
class one():
    def fun3(self):
        cse.fun1(self)
    def fun4(self):
        print("three")
a=one()
a.fun3()'''

#longest palindromic string
def palin(str):
    def rev(left,right):
        while left>=0 and right<len(str) and str[left]!=str[right]:
            left-=1
            right+=1
        return str[left+1:right-1]
    res=[]
    for i in range(len(str)):
        pal1=rev(i,i)
        if len(pal1)>1:
            res.append(pal1)
        pal2=rev(i,i+1)
        if len(pal2)>1:
            res.append(pal2)
    return res
str=input()
k=palin(str)
print(k)

#oops:
'''
class cse:
    def _init_(self,a):
        self.a=a
        print("welcome",a)
    def fun(s):
        print("hello",s.a)
o=cse(2)
b=cse(5)
#o._init_(4)#constructor can be created with object also 
o.fun()
'''


#opps-inheritance
'''
class zero:
    def funa(self):
        print("yes")
    def funb(self):
        print("no")

class one:
    def fun1(self):
        print("func1")
    def fun2(self):
        print("func2")

class two(one):
    def fun3(self):
        print("func3")
    def fun4(self):
        print("func4")
        
class three(zero,two):
    def fun5(self):
        print("func5")
    def fun6(self):
        print("func6")
#ob creation
a=one()
b=two()
c=three()
#calling
a.fun1()
a.fun2()
b.fun1()
b.fun2()
b.fun3()
b.fun4()
c.fun1()
c.fun2()
c.fun3()
c.fun4()
c.funa()
c.funb()
c.fun5()
c.fun6()
'''


#call the class inside a class using class_name.func_name
'''
class zero:
    def funa(self):
        print("yes")
    def funb(self):
        print("no")

class one:
    def fun1(self):
        zero.funa(self)#calling the (class_name.fun_name)
        print("func1")
    def fun2(self):
        print("func2")

obj=one()
obj.fun1()#fun1 and funa is executed
obj.fun2()
'''



#super class:
'''
class one:
    def fun1(self):
        print("1 Hello")
    def fun2(self):
        print("2Hello")

class two(one):
    def fun3(self):
        super().fun1()
    def fun4(self):
        print("4 Hello")

a=two()
a.fun3()
a.fun4()
'''

#class addition:
#    def ope(self,a,b):
#        print(a+b)
#    def ope(self,a,b,c):
#        print(a+b+c)
#    def ope(self,a,b,c,d):
#        print(a+b+c+d)

#a=addition()
#a.ope(10,20,30,40)#python doesn't support method overloading




