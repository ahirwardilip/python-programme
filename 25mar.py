'''
class MyMath():
    def add1(self):
        a=int(input("Enter Number:"))
        b=int(input("Enter Number:"))
        c=a+b
        print("Sum is:",c)
    def add2(self,a,b):
        print("Sum is:",a+b)
    def add3(self):
        a=int(input("Enter Number:"))
        b=int(input("Enter Number:"))
        return a+b
    def add4(self,a,b):
        return a+b
m=MyMath()
m.add1()
m.add2(4,5)
print(m.add3())
print(m.add4(4,5))
'''

'''
class MyMath():
    def table1(self):
        n=int(input("Enter number:"))
        i=1
        while i<11:
            print(i*n)
            i+=1
    def fact1(self):
        n=int(input("Enter number:"))
        f=1
        while n>1:
            f=f*n
            n-=1
        print("Factorial is:",f)
    def table2(self,n):
        i=1
        while i<11:
            print(i*n)
            i+=1
    def fact2(self,n):
        f=1
        while n>1:
            f=f*n
            n-=1
        print("Factorial is:",f)
            
        
m=MyMath()
m.table1()
m.fact1()
m.table2(5)
m.fact2(6)
'''

'''
class Bank():
    def getinfo(self):
        acc=int(input("Enter account number:"))
        n=input("Enter Name:")
        bal=float(input("Enter balance:"))

        print("Account Number:",acc)
        print("Name:",n)
        print("Balance:",bal)
b=Bank()
b.getinfo()
'''
