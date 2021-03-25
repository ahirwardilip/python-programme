'''
def show(n):
    f1=0
    f2=1
    print(f1,end=' ')
    print(f2,end=' ')
    f=f1+f2
    while f<n:
        print(f,end=' ')
        f1=f2
        f2=f
        f=f1+f2
n=int(input("Enter number:"))
show(n)
'''
'''
def rev(l):
    l1=[]
    i=0
    while i<len(l):
        l1.append(l[len(l)-i-1])
        i=i+1
    return l1
l=[1,2,3,4,5]
r=rev(l)
print(r)
'''

#OOPS concept:It is used to perform operations according to object or it is used to follow real time programming
#approach .It provides many concepts such as class, object, data binding, data hiding, encapsulation, inheritance,
#polymorphism,abstraction,message passing....etc.

#Class:It is a factory which produce object.
#It is a collection of similar type objects.
#It contains public private data members and member functions.

#Syntax:-
#    class <class_name>:
#        ===
#        ===

#Object:It is a real world entity or instance of the class.

#Syntax:
#    <obj>=<class_name>()

'''
class Myclass:
    def show():
        print("Hello... Python")
m=Myclass()
m.show()
'''

'''
class Myclass:
    def show(self):
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        c=a+b
        print(c)
m=Myclass()
m.show()
'''
