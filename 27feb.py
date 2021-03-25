#While loop(syntax):-
#        while <exp>:
#            ===
#            ===

#Print 1 2 3 4 5.

'''
i=1
while i<=5:
    print(i)
    i+=1
'''

#Write a program to print mathematical table of any number.

'''
a=int(input("Enter Number:"))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1
'''

#Write a program to find out factorial of any number.

'''
n=int(input("Enter Number:"))
i=n-1
while i>0:
    n=n*i
    i-=1
print(n)
'''

'''
n=int(input("Enter Number:"))
f=1
while n>1:
    f=f*n
    n=n-1
print(f)
'''

#Write a program to find out sum of first n numbers and also find out their average.

'''
n=int(input("Enter Number:"))
i=1
s=0
while i<=n:
    s+=i
    i+=1
print(s)
'''

#Write a program to find sum from n1 to n2.

'''
n1=int(input("Enter Number:"))
n2=int(input("Enter Number:"))
s=0
while n1<=n2:
    s+=n1
    n1+=1
print(s)
avg=s/(n2-n1+1)
'''

'''
n1=int(input("Enter Number:"))
n2=int(input("Enter Number:"))
i=n1
s=0
while i<=n2:
    s=s+i
    i=i+1
print("Sum is:"+str(s))
avg=s/(n2-n1+1)
print("Avg is:"+str(avg)
'''

#Print 1 1 1 2 4 8 3 9 27 . . . . . . n n^2 n^3.
'''
n=int(input("Enter Number:"))
i=1
while i<=n:
    print(i," ",i*i," ",i*i*i," ",end=" ")
    i=i+1
'''
