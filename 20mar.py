# 1.No argument and no return type
'''
def fact():
    n=int(input("Enter any Number:"))
    f=1
    while n>1:
        f=f*n
        n-=1
    print(f)
fact()    
'''

# 2.argument and no return type
'''
def fact(n):
    f=1
    while n>1:
        f=f*n
        n-=1
    print(f)
n=int(input("Enter any Number:"))
fact(n)
'''

# 3.No argument and return type 
'''
def fact():
    n=int(input("Enter any Number:"))
    f=1
    while n>1:
        f=f*n
        n-=1
    return f
r=fact()
print("Factorial is:",r)
print("Factorial is:",fact())
'''

# 4.argument and return type
'''
def fact(n):
    f=1
    while n>1:
        f=f*n
        n-=1
    return f
n=int(input("Enter any Number:"))
r=fact(n)
print("Factorial is:",r)
'''

'''
def add():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a+b
    avg=(a+b)/2
    return c,avg
r,g=add()
print("Sum is",r)
print("Average is",g)
'''

'''
def add():
    l=[]
    temp=True
    while temp:
        i=int(input("Enter element:"))
        l.append(i)
        op=int(input("Do u want to insert more elements....Press 1.Yes 2.No"))
        if op==1:
            temp=True
        else:
            temp=False
    print("List is",l)    
    c=sum(l)
    d=sum(l)/len(l)
    e=len(l)

    return c,d,e

r=add()
print(r)
'''

